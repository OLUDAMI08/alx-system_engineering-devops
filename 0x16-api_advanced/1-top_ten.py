#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers """

import requests
import sys


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Google chrome'}
    # Set a custom User-Agent to avoid Too Many Requests error

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        child_data = data.get('data').get('children')
        for entry in child_data:
            print(entry.get('data').get('title'))
    else:
        print(None)
