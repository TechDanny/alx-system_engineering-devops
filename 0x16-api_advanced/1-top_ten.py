#!/usr/bin/python3
"""
queries the reddit API and returns the numbers of subscribers
"""


import requests


def top_ten(subreddit):
    """if not valid print none"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My user Agent 1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for n in range(10):
                print(children[n].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
