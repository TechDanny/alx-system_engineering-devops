#!/usr/bin/python3
"""
queries the reddit API and returns the numbers of subscribers
"""


import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My user Agent 1.0"}
    response = requets.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        return data.get("subscribers", 0)
    else:
        return 0
