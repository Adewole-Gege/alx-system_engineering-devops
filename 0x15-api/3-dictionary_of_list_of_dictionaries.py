#!/usr/bin/python3
"""Exports all employees' tasks into a structured JSON file."""
import json
import requests


def export_all_tasks():
    base_url = "https://jsonplaceholder.typicode.com/"
    try:
        users = requests.get(f"{base_url}users").json()
        all_tasks = {}

        for user in users:
            tasks = requests.get(
                f"{base_url}todos", params={
                    "userId": user['id']}).json()
            all_tasks[user['id']] = [{
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed']
            } for task in tasks]

        with open("todo_all_employees.json", 'w') as file:
            json.dump(all_tasks, file)
    except requests.RequestException:
        print("Failed to retrieve or write data.")


if __name__ == "__main__":
    export_all_tasks()
