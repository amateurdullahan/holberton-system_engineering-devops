#!/usr/bin/python3
"""2 but make it a dictionary list of dictionaries"""
import json
from requests import get

if __name__ == "__main__":
    nurl = 'https://jsonplaceholder.typicode.com/users'
    turl = 'https://jsonplaceholder.typicode.com/todos'
    names = get(nurl).json()
    todos = get(turl)

    o_dict = {}
    wlist = []
    wl_dict = {}
    user = 1
    for name in names:
        for todo in todos.json():
            if user == todo.get("userId"):
                wl_dict.update({"task": todo.get("title")})
                wl_dict.update({"completed": todo.get("completed")})
                wl_dict.update({"username": name.get("username")})
                wlist.append(wl_dict)
                wl_dict = {}

        o_dict.update({name.get("id"): wlist})
        wlist = []
        user += 1

    with open('todo_all_employees.json', 'w') as file:
        json.dump(o_dict, file)
