#!/usr/bin/python3

'''
Function to query Reddit API
'''
import requests


def number_of_subscribers(subreddit):
    '''
    Return the total number of subscribers on a given subreddit
    '''
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    print(url)

    user_agent = 'Mozilla/5.0'
    headers = {'User-Agent': user_agent}

    response = requests.get(url, headers=headers, allow_redirects=False)

    print(response.status_code)

    if response.status_code != 200:
        return 0

    results = response.json()["data"]["subscribers"]
    return results
