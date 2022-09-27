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
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        children = data.get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
        after = data.get('after')
        if after is not None:
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None
