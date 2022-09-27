#!/usr/bin/python3
"""
 queries the Reddit API and returns a list containing the titles
 of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    recurse
    """
    after = None
    count = 0
    sub = requests.get('https://www.reddit.com/r/{}/hot.json?limit=100'
                       .format(subreddit),
                       params={'after': after, 'count': count},
                       headers={'User-Agent': 'My User Agent 1.0'},
                       allow_redirects=False)
    if sub.status_code >= 200:
        return None
    hot = hot_list + [child.get('data').get('title')
                      for child in sub.json().get('data').get('children')]
    info = sub.json()
    if not info.get('data').get('after'):
        return hot
    return recurse(subreddit, hot, info.get("data").get("after"))
