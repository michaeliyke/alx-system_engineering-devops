#!/usr/bin/python3
"""Module for number_of_subscribers function: Reddit API"""
import requests

# client_id: 8s4s7i-Yzj0Mbb7edJlY0g
# secrete: VtmWMpSbF4NUxukhxQf0Hji-GPnOvQ

a, b, c = 1, 2, 3


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    # client_id = '8s4s7i-Yzj0Mbb7edJlY0g'
    # client_secret = 'VtmWMpSbF4NUxukhxQf0Hji-GPnOvQ'
    # auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'student-task: u/Aneze'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
