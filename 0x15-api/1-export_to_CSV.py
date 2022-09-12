#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in the CSV format.
"""

import requests
import urllib
import csv

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
    with open('{}.csv'.format(user_id), 'w') as csv_file:
        writer = csv.writer(csv_file)
        for task in todos:
            if task.get('completed'):
                writer.writerow([user_id, user_name, task.get('title'),
                                 task.get('completed')])
