#!/usr/bin/python3
"""API 0"""
from requests import get
from sys import argv


if __name__ == '__main__':
    nurl = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    turl = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    EMPLOYEE_NAME = get(nurl).json().get("name")
    todo = get(turl)
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = len(todo.json())
    comlist = []

    for task in todo.json():
        if task.get("completed"):
            NUMBER_OF_DONE_TASKS += 1
            comlist.append(task.get("title"))

    line_1 = "Employee {} is done with tasks({}/{}):".format(
                EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS)
    print(line_1)

    for com in comlist:
        print("\t {}".format(com))
