#!/usr/bin/python3
"""Export an employee's tasks to a CSV file based on their ID."""
import csv
import requests
import sys


def export_tasks_to_csv(user_id):
    api_url = "https://jsonplaceholder.typicode.com/"
    try:
        user_response = requests.get(f"{api_url}users/{user_id}")
        if user_response.status_code != 200:
            print("Failed to retrieve user data")
            return

        user = user_response.json()
        todos_response = requests.get(
            f"{api_url}todos", params={
                "userId": user_id})
        if todos_response.status_code != 200:
            print("Failed to retrieve todos data")
            return

        todos = todos_response.json()

        with open(f"{user_id}.csv", 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for todo in todos:
                writer.writerow([user_id, user['username'],
                                todo['completed'], todo['title']])
    except requests.RequestException as e:
        print(f"HTTP Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <user_id>")
        sys.exit(1)

    export_tasks_to_csv(sys.argv[1])
