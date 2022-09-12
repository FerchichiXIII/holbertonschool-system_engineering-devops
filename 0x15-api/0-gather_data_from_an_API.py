#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    user = requests.get(url).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        argv[1])
    tasks = requests.get(url).json()
    done_tasks = [task for task in tasks if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_tasks), len(tasks)))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
