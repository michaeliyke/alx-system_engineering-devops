#!/usr/bin/python3
"""Returns information about an employee's TODO list progress using an API"""
import json
import requests
import sys


def user(id) -> dict:
    """Get the information of the user with the given ID."""
    info = f"https://jsonplaceholder.typicode.com/users/{id}"
    return requests.get(info).json()


def todos(id) -> list:
    """Get the TODO list of the user with the given ID."""
    ID = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{ID}/todos"
    req = requests.get(url)
    return req.json()


def display(tasks, user) -> None:
    """Display the information in the required format."""
    total = len(tasks)
    completed = len([task for task in tasks if task.get('completed')])
    message = "Employee {} is done with tasks({}/{}):"
    print(message.format(user.get('name'), completed, total))
    for task in tasks:
        print("\t " + task.get('title'))


def export_csv(tasks, user) -> None:
    """Export the information in CSV format."""
    with open(f"{user.get('id')}.csv", "w") as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'.format(
                user.get('id'), user.get('username'),
                task.get('completed'), task.get('title')))


def export_json(tasks, user) -> None:
    """Export employee tasks to json"""
    data = {}
    data[user.get("id")] = []

    for task in tasks:
        tsk = {}
        tsk["username"] = user.get("username")
        tsk["task"] = task.get("title")
        tsk["completed"] = task.get("completed")
        data[user.get("id")].append(tsk)
    return json.dumps(data)


if __name__ == "__main__":
    data = export_json(todos(sys.argv[1]), user(sys.argv[1]))
    with open(f"{sys.argv[1]}.json", "w") as file:
        file.write(data)
