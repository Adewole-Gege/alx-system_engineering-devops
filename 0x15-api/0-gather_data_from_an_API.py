#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    try:
        user_url = url + "users/{}".format(sys.argv[1])
        todos_url = url + "todos"

        user_response = requests.get(user_url)
        # Raises an HTTPError for bad responses
        user_response.raise_for_status()

        todos_response = requests.get(
            todos_url, params={"userId": sys.argv[1]}
        )
        todos_response.raise_for_status()

        user = user_response.json()
        todos = todos_response.json()

        completed = [task['title']
                     for task in todos if task.get('completed', False)]

        task_summary = "Employee {} is done with tasks({}/{}):".format(
            user.get('name'), len(completed), len(todos)
        )
        print(task_summary)

        for completed_task in completed:
            print("\t {}".format(completed_task))

    except requests.RequestException as e:
        print("HTTP Request failed: {}".format(e))
