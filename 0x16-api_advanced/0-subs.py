#!/usr/bin/python3
"""like and subscribe"""
from requests import get


def number_of_subscribers(subreddit):
    """return number of subs in subreddit"""
    rurl = "https://www.reddit.com/r/{}/about.json".format(subreddit)
