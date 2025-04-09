#!/usr/bin/python3
"""
Module to interact with the Reddit API and get subreddit subscriber count.
"""
import requests

# Custom User-Agent to avoid Reddit API rate limits
HEADERS = {"User-Agent": "ALX-Project-RedditAPI/1.0"}


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the total number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The subreddit name.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, allow_redirects=False, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0  # Return 0 if subreddit is invalid or inaccessible
    except requests.exceptions.RequestException:
        return 0  # Return 0 in case of any network/API errors
