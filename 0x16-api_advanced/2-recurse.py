#!/usr/bin/python3
'''
Modue containing recursive function that
queries the Reddit API and returns a list containing
the titles of all hot articles for a subreddit
'''
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Returns a list of titles of all hot posts on a given subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    user_agent = 'Mozilla/5.0'
    headers = {'User-Agent': user_agent}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
