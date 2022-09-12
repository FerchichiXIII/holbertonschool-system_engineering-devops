#!/usr/bin/python3
"""
using this REST API, for a given employee ID, returns information about his/her TODO list progress.
"""

import requests
import urllib


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos'
    user_id = '1'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(user_url).json()
    user_name = user.get('name')
    todos = requests.get(url, params={'userId': user_id}).json()
    total_tasks = len(todos)
    completed_tasks = 0
    for task in todos:
        if task.get('completed'):
            completed_tasks += 1
    print('Employee {} is done with tasks({}/{}):'.format(user_name,
          completed_tasks, total_tasks))
    for task in todos:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
