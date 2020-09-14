#!/usr/bin/python3
"""0 but make it CSV"""
import csv
from requests import get
from sys import argv


if __name__ == '__main__':
    nurl = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    turl = "https://jsonplaceholder.typicode.com/todo?userId=" + argv[1]
    EMPLOYEE_NAME = get(nurl).json().get("name")
    todo = get(turl)
    names = get(nurl).json()
    filename = "{}.csv".format(argv[1])
    with open(filename, 'w', newline='') as file:
        write = csv.writer(file, quoting=csv.QUOTE_ALL)
        wlist = []
        for task in todo.json():
            wlist.append(names.get("id"))
            wlist.append(names.get("username"))
            wlist.append(task.get("completed"))
            wlist.append(task.get("title"))
            write.writerow(wlist)
            wlist = []
