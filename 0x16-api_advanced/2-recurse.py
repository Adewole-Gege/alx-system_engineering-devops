#!/usr/bin/python3
"""
Queries the Reddit API recursively to return a list of all hot article titles
for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches all hot article titles for a given subreddit.

    Args:
        subreddit (str): The subreddit name.
        hot_list (list): A list to store the titles.
        after (str): A pagination parameter for Reddit API.

    Returns:
        list: A list of all hot article titles,
        or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditClient/1.0"}
    params = {"limit": 100, "after": after}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {})
        children = data.get("children", [])
        hot_list.extend(post["data"]["title"] for post in children)

        # Recursively call the function with the next 'after' value
        after = data.get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
