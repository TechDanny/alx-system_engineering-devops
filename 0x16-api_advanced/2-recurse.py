#!/usr/bin/python3
"""
Queries Reddit API and returns the list containing all the titles
"""


import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """if not valid return None"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {
            "after": after,
            "count": count,
            "limit": 100
            }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    rslt = response.json().get('data')
    after = rslt.get('after')
    count += rslt.get('dist')
    for i in rslt.get("children"):
        hot_list.append(i.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    else:
        return hot_list
