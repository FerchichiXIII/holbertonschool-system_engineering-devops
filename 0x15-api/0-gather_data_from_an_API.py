#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":

    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/todos/users/{}".format(user_id))
    name = user.json().get('name')
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    total_tasks = 0
    completed = 0

    for task in todos.json():
        if task.get('user_id') == int(user_id):
            completed =+ 1
    
    print('Employee {} is done with task({}/{}):'
                    .format(name, completed, total_tasks))
    
    print('\n'.join(["\t " + task.get("title") for task in todos.json()
        if task.get("user_id") == int(user_id) and task.get("completed")]))
