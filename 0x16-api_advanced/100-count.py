#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses hot article titles,
and counts keyword occurrences (advanced task).
"""
import requests
import re


def count_words(subreddit, word_list, after=None, counts=None, freq=None):
    """
    Recursively queries the Reddit API, parses titles of all hot articles,
    and counts occurrences of each keyword in word_list (case-insensitive).

    Prints results in descending order by count, then ascending order by word.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): List of words to search for in post titles.
        after (str): The "after" pagination token, used in recursive calls.
        counts (dict): Running tally of counts for each keyword.
        freq (dict): Frequency map for handling duplicates in word_list.

    Returns:
        None. (Prints output or prints nothing
        if subreddit invalid / no matches.)
    """

    # On the first call, initialize everything
    if counts is None:
        counts = {}
    if freq is None:
        # freq holds how many times each (lowercased) word appears in word_list
        freq = {}
        for w in word_list:
            lw = w.lower()
            freq[lw] = freq.get(lw, 0) + 1
            # Ensure counts dict has the key, but 0 to start
            if lw not in counts:
                counts[lw] = 0

    # Base URL with pagination
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyRedditClient/1.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    # Make the request
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)
    if response.status_code != 200:
        # Invalid subreddit or some other error → do not print anything
        return

    # Parse JSON
    data = response.json().get("data", {})
    children = data.get("children", [])
    after = data.get("after", None)

    # Use regex to split titles into alphanumeric "words" only
    # This ensures "javascript" won't match "java," etc.
    for post in children:
        title = post["data"]["title"].lower()
        words_in_title = re.findall(r"\w+", title)
        for w in words_in_title:
            # If this word is in freq, increment count by freq[w]
            # freq[w] might be > 1 if duplicates were in word_list
            if w in freq:
                counts[w] += freq[w]

    # If there's a next page, recurse; otherwise, print final results
    if after is not None:
        return count_words(subreddit, word_list, after, counts, freq)
    else:
        # All pages processed, now we sort and print

        # Filter out zero-count words
        filtered = [(word, cnt) for word, cnt in counts.items() if cnt > 0]

        # Sort by count DESC, then word ASC
        sorted_counts = sorted(filtered, key=lambda x: (-x[1], x[0]))

        # Print in the required format
        for word, cnt in sorted_counts:
            print("{}: {}".format(word, cnt))
