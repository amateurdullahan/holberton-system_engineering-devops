#!/usr/bin/python3
"""like and subscribe"""
from requests import get


def number_of_subscribers(subreddit):
    """return number of subs in subreddit"""
    rurl = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = get(rurl, allow_redirects=False, headers={'User-agent': ''})
    if req.json().get("kind") == "t5":
        data = req.json().get("data")
        return data.get("subscribers")
    else:
        return 0
