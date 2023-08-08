#!/usr/bin/python3

'''
Module containing the function that fecthes the first
10 posts of a subreddit
'''
import requests


def top_ten(subreddit):
    '''
    Returns the first 10 hottest posts of a sebreddit

    Args:
        Subreddit (string): Containing the posts to be checked
    '''
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    user_agent = 'Mozilla/5.0'
    headers = {'user_agent': user_agent}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print('None')
        return

    results = response.json()['data']
    [print(c.get("data").get("title")) for c in results.get("children")]
