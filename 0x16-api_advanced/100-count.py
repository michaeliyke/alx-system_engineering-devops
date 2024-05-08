#!/usr/bin/python3
"""Module for number_of_subscribers function: Reddit API"""
import requests

headers = {'User-Agent': 'student-task: u/Aneze'}


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')


def top_ten(subreddit):
    """Get the top 10 hot posts for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get('data')
    posts = data.get('children')
    for post in posts[:10]:
        print(post.get('data').get('title'))


def recurse(subreddit, hot_list=[]):
    """Get all hot posts for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get('data')
    posts = data.get('children')
    for post in posts:
        hot_list.append(post.get('data').get('title'))
    after = data.get('after')
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list)


def get_hits_count_desc(words: list, sentences: list) -> dict:
    """Get a dict of keyword counts"""
    counts = {word: 0 for word in words}  # Initialize counts to 0
    for word in words:
        sentence: str
        for sentence in sentences:
            counts[words] += sentence.count(word)

    # Remove those with count of 0
    for word in words:
        if counts[word] == 0:
            del counts[word]

    # Sort counts
    sorted_dict = dict(sorted(counts.items(), reverse=True,
                              key=lambda tpl: tpl[1]))
    return sorted_dict


def count_words(subreddit: str, word_list: str, titles=None):
    """Count occurences of keywords in words_list using hot_list titles"""

    if (titles is None):
        titles = []

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None
    data = response.json().get('data')
    posts = data.get('children')

    for post in posts:
        titles.append(post.get('data').get('title'))
    after = data.get('after')

    if after is None:
        words: list = sorted(word_list.split())
        sorted_hits: dict = get_hits_count_desc(words, titles)
        for key, val in sorted_hits.items():
            print(f"{key}: {val}")
        return titles

    return recurse(subreddit, titles)
