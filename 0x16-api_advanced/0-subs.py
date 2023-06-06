#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers """

import requests
import sys


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Google chrome'}
    # Set a custom User-Agent to avoid Too Many Requests error

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data.get('data').get('subscribers')
        return (subscribers)

    return (0)
