#!/usr/bin/python3
"""1 but make it export to JSON"""
import json
from requests import get
from sys import argv

if __name__ == "__main__":
    nurl = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    turl = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    names = get(nurl).json()
    todos = get(turl)

    output_dict = {}
    wlist = []
    wl_dict = {}
    for todo in todos.json():
        wl_dict.update({"task": todo.get("title")})
        wl_dict.update({"completed": todo.get("completed")})
        wl_dict.update({"username": names.get("username")})
        wlist.append(wl_dict)
        wl_dict = {}

    output_dict.update({names.get("id"): wlist})

    fname = "{}.json".format(argv[1])
    with open(fname, 'w') as file:
        json.dump(output_dict, file)
