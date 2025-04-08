#!/usr/bin/python3
"""Export an employee's tasks to a JSON file."""
import json
import requests
import sys


def export_tasks_to_json(user_id):
    api_url = "https://jsonplaceholder.typicode.com/"
    try:
        user = requests.get(f"{api_url}users/{user_id}").json()
        tasks = requests.get(
            f"{api_url}todos", params={
                "userId": user_id}).json()

        tasks_data = [{
            "task": task['title'],
            "completed": task['completed'],
            "username": user['username']
        } for task in tasks]

        with open(f"{user_id}.json", 'w') as json_file:
            json.dump({user_id: tasks_data}, json_file)
    except requests.RequestException:
        print("Failed to retrieve or write data.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <user_id>")
        sys.exit(1)
    export_tasks_to_json(sys.argv[1])
