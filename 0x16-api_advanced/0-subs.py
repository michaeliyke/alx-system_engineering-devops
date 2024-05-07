#!/usr/bin/python3
"""Module for number_of_subscribers function: Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'student-task: u/Aneze'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    for key in response.json().get('data').keys():
        print(key)
    return response.json().get('data').get('subscribers')
