import os

# Define the data structure for tasks
tasks = []

# Function to display the main menu
def show_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Complete/Uncomplete")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Exit")

# Function to add a task
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {"title": title, "description": description, "completed": False}
    tasks.append(task)
    print("Task added successfully!")

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTask List:")
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i+1}. Title: {task['title']}, Description: {task['description']}, Status: {status}")

# Function to mark a task as complete/uncomplete
def mark_task():
    list_tasks()
    try:
        task_index = int(input("Enter the task number to mark as complete/uncomplete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = not tasks[task_index]["completed"]
            print("Task status updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to delete a task
def delete_task():
    list_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to save tasks to a text file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['title']}|{task['description']}|{task['completed']}\n")
    print("Tasks saved to 'tasks.txt'.")

# Function to load tasks from a text file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            tasks.clear()
            for line in lines:
                title, description, completed = line.strip().split("|")
                tasks.append({"title": title, "description": description, "completed": completed == "True"})
        print("Tasks loaded from 'tasks.txt'.")
    else:
        print("No saved tasks found.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-7): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        mark_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        save_tasks()
    elif choice == "6":
        load_tasks()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")
