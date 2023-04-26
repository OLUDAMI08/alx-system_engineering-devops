import requests
import sys

# Set up the base URL for the API
BASE_URL = 'https://jsonplaceholder.typicode.com'

# Get the employee ID from the command line arguments
employee_id = sys.argv[1]

# Make a request to the API to get the employee information
employee_response = requests.get('{}/users/{}'.format(BASE_URL, employee_id))
employee_data = employee_response.json()
employee_name = employee_data['name']

# Make a request to the API to get the employee's TODO list
todo_response = requests.get('{}/todos?userId={}'
                             .format(BASE_URL, employee_id))
todo_data = todo_response.json()
total_tasks = len(todo_data)

# Count the number of completed tasks
completed_tasks = [task for task in todo_data if task['completed']]
num_completed_tasks = len(completed_tasks)

# Display the employee TODO list progress
print('Employee {} is done with tasks({}/{}):'
      .format(employee_name, num_completed_tasks, total_tasks))
for task in completed_tasks:
    print('\t {}'.format(task['title']))
