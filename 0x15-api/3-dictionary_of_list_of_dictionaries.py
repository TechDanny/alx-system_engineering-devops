#!/usr/bin/python3
"""
Export data into json format
"""


from json import dump
from requests import get


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = get(url + "users").json()

    with open("todo_all_employees.json", "w") as f:
        dump({
             x.get("id"): [{
                 "task": n.get("title"),
                 "completed": n.get("completed"),
                 "username": x.get("username")
             } for n in get(url + "todos",
                            params={"userId": x.get("id")}).json()]
             for x in users}, f)
