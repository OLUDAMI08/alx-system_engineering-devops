#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns titles"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Google chrome"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        child_data = data.get('data').get('children')
        for entry in child_data:
            hot_list.append(entry.get('data').get('title'))

        # Check if there a next page
        after = data.get('data').get('after')
        if after:
            recurse(subreddit, hot_list=hot_list, after=after)

    else:
        return None

    return hot_list
