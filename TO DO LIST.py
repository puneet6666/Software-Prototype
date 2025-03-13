from datetime import datetime
import json

# Task list - in-memory storage simulation
tasks = []

def display_tasks():
    print("\nCurrent Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}: {task['name']} - Priority: {task['priority']} - Due: {task['due_date']} - Description: {task['description']}")

def add_task():
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    priority = input("Enter task priority (High, Medium, Low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    task = {
        "name": name,
        "description": description,
        "priority": priority,
        "due_date": due_date
    }
    tasks.append(task)
    print("Task added successfully.")

def edit_task():
    display_tasks()
    task_index = int(input("Enter the task number to edit: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        return
    print("\nEditing Task:", tasks[task_index]['name'])
    tasks[task_index]['name'] = input("Enter new task name: ")
    tasks[task_index]['description'] = input("Enter new description: ")
    tasks[task_index]['priority'] = input("Enter new priority (High, Medium, Low): ")
    tasks[task_index]['due_date'] = input("Enter new due date (YYYY-MM-DD): ")
    print("Task updated successfully.")

def delete_task():
    display_tasks()
    task_index = int(input("Enter the task number to delete: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        return
    del tasks[task_index]
    print("Task deleted successfully.")

def main_menu():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Display All Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            edit_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            display_tasks()
        elif choice == '5':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
