#!/usr/bin/python3
"""TOP TEN ANIME BETRAYALS"""
from requests import get


def top_ten(subreddit):
    """return top ten in subreddit"""
    rurl = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
