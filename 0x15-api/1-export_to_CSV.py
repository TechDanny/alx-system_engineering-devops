#!/usr/bin/python3
"""
Export data in CSV format
"""


import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    username = response.json().get('username')

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    response = requests.get(url)
    tasks = response.json()
    with open("{}.csv".format(user_id), 'w') as f:
        for x in tasks:
            f.write('"{}","{}","{}","{}"\n'.format(user_id,
                    username, x.get("completed"), x.get("title")))
