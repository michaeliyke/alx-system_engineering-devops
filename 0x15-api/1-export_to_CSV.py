#!/usr/bin/python3
"""Returns information about an employee's TODO list progress using an API"""
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


def display(data, user) -> None:
    """Display the information in the required format."""
    total = len(data)
    completed = len([task for task in data if task.get('completed')])
    message = "Employee {} is done with tasks({}/{}):"
    print(message.format(user.get('name'), completed, total))
    for task in data:
        print("\t " + task.get('title'))


def export_csv(data, user) -> None:
    """Export the information in CSV format."""
    with open(f"{user.get('id')}.csv", "w") as file:
        for task in data:
            file.write('"{}","{}","{}","{}"\n'.format(
                user.get('id'), user.get('username'),
                task.get('completed'), task.get('title')))


if __name__ == "__main__":
    export_csv(todos(sys.argv[1]), user(sys.argv[1]))
