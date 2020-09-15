#!/usr/bin/python3
"""0 but make it CSV"""
import csv
from requests import get
from sys import argv


if __name__ == '__main__':
    nurl = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    turl = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    names = get(nurl).json()
    todos = get(turl)
    fname = "{}.csv".format(argv[1])

    with open(fname, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        wlist = []

        for todo in todos.json():
            wlist.append(names.get("id"))
            wlist.append(names.get("username"))
            wlist.append(todo.get("completed"))
            wlist.append(todo.get("title"))
            writer.writerow(wlist)
            wlist = []
