#!/usr/bin/python3
"""Module for number_of_subscribers function: Reddit API"""
import requests

headers = {'User-Agent': 'student-task: u/Aneze'}


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    try:
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        return response.json().get('data').get('subscribers')
    except Exception as e:
        return 0


def top_ten(subreddit):
    """Get the top 10 hot posts for a given subreddit"""

    try:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        data = response.json().get('data')
        posts = data.get('children')
        for post in posts[:10]:
            print(post.get('data').get('title'))
    except Exception as e:
        print(None)
