#!/usr/bin/python3
"""
Export data in the JSON format
"""


import requests
import sys
import json


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    username = response.json().get("username")

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    response = requests.get(url)
    tasks = response.json()
    my_dict = {user_id: []}
    for n in tasks:
        my_dict[user_id].append({
                                 "task": n.get('title'),
                                 "completed": n.get('completed'),
                                 "username": username
                                 })
    with open("{}.json".format(user_id), 'w') as f:
        json.dump(my_dict, f)
