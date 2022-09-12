#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in the JSON format.
"""

import json
import requests
import sys



if __name__ == "__main__":
	url = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
	r = requests.get(url)
	user = r.json()
	url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(sys.argv[1])
	r = requests.get(url)
	tasks = r.json()
	data = []
	for task in tasks:
		data.append({
			"task": task.get('title'),
			"completed": task.get('completed'),
			"username": user.get('username')
		})
	with open('{}.json'.format(sys.argv[1]), 'w') as f:
		json.dump({sys.argv[1]: data}, f)

