import json
import os

TASK_FILE = '../tasks.json'

if not os.path.exists(TASK_FILE):	
	with open(TASK_FILE, 'w') as file:
		json.dump([], file)

def load_tasks():
	with open(TASK_FILE, 'r') as file:
		return json.load(file)
	
def save_tasks(tasks):
	with open(TASK_FILE, 'w') as file:
		json.dump(tasks, file, indent=2)

def add_task():
	task_name = input('Enter the task name : ').strip()
	tasks = load_tasks()
	tasks.append({"task": task_name, "status": "Incomplete"})
	save_tasks(tasks)
	print(f'Task "{task_name} added successfully!"')

def view_tasks():
	tasks = load_tasks()
	if tasks:
		print("\n--- Task List ---")
		for idx, task in enumerate(tasks, start=1):
			print(f"{idx}. {task['task']} - {task['status']}")
	else:
		print("No tasks found.")

def update_status():
	tasks = load_tasks()
	view_tasks()
	try:
		task_index = int(input("Enter the task number to update : ")) - 1
		if 0 <= task_index < len(tasks):
			new_status = input("Enter the new status : ").strip()
			tasks[task_index]['status'] = new_status
			save_tasks(tasks)
			print("Task status updated successfully!")
		else:
			print("Invalid task number!")
	except Exception as e:
		print("Error : %s",e)

def delete_task():
	tasks = load_tasks()
	view_tasks()
	try:
		task_index = int(input("Enter the task number to delete : ")) - 1 
		if 0 <= task_index < len(tasks):
			deleted_task = tasks.pop(task_index)
			save_tasks(tasks)
			print(f'Task "{deleted_task["task"]}" deleted successfully!')
		else:
			print("Invalid task number!")
	except Exception as e:
		print("Error : %s",e)

def display_menu():
	print("\n--- Task App ---")
	print("1. Add Task")
	print("2. View Tasks")
	print("3. Update Task Status")
	print("4. Delete Task")
	print("5. Exit\n")

while True:
	display_menu()
	choice = input("Enter your choice : ").strip()
	if choice == '1':
		add_task()
	elif choice == '2':
		view_tasks()
	elif choice == '3':
		update_status()
	elif choice == '4':
		delete_task()
	elif choice == '5':
		print("Exiting the app. Goodbye!")
		break
	else:
		print("Invalid choice! Please try again.")