#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    top ten
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for i in range(10):
            print(response.json().get('data').get('children')[i].get('data')
                  .get('title'))
    else:
        print(None)
