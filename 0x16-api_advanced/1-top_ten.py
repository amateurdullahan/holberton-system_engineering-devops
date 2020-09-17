#!/usr/bin/python3
"""TOP TEN ANIME BETRAYALS"""
from requests import get


def top_ten(subreddit):
    """return top ten in subreddit"""
    rurl = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": ''}
    params = {"limit": 10}
    request = get(rurl, headers=headers, params=params, allow_redirects=False)
    if request.status_code == 404:
        print("None")
        return
    results = request.json().get("data")
    for result in results.get("children"):
        print(result.get("data").get("title"))
