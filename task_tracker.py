import os
import json
import argparse
from datetime import datetime


# JSON AS DB to store user tasks
TASKS_FILE = "task-tracker.json"

# AVAILABLE STATUS
VALID_STATUS = ["to-do", "mark-in-progress", "done"]

# LOAD FILE
def load_tasks():
    """Load the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    
    return {"last_id": 0, "tasks":[]}


# SAVE DATA to file
def save_tasks(data):
    """Save tasks to JSON file"""
    with open(TASKS_FILE, 'w') as file:
        json.dump(data, file, indent=4)


def current_time():
    return datetime.now().isoformat()
        

def add_task(description):
    """Add tasks to file"""
    if not description.strip():
        print("\n❌ Error: Task description cannot be empty")
        return

    data = load_tasks()

    data["last_id"] += 1
    task_id = data["last_id"]

    timestamp = current_time()

    data["tasks"].append(
        {
            "id": task_id,
            "description": description,
            "status":"to-do",
            "createdAt": timestamp,
            "updatedAt": timestamp
        }
    )

    save_tasks(data)
    print(f"\n✅ Task successfully added. \nTask ID : {task_id} \nDescription : '{description}' \nStatus : to-do")


def update_tasks(task_id, new_description):
    """Update tasks"""
    if not new_description.strip():
        print("\n❌ Error: Task description cannot be empty")
        return

    data = load_tasks()

    for task in data['tasks']:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = current_time()
            
            save_tasks(data)
            
            print(f"\n✅ Task successfully updated. \nTask ID : {task_id} \nDescription : {new_description}")
            return
    else:
        print(f"No task found with ID: {task_id}")

def delete_tasks(task_id):
    """Allow users to delete tasks."""
    
    data = load_tasks()
    
    # CHECK IF TASK IS EMPTY
    if not data['tasks']:
        print("\n🔴 Error: The file is empty! Please enter a task first.")
        return
    
    for task in data['tasks']:
        if task['id'] == task_id:
            data['tasks'].remove(task)
        
            save_tasks(data)
            
            print(f"\n✅ Task ID: {task_id} successfully deleted")
            break
    else:
        print("\n❌ Task not found.")


def task_in_progress(task_id, description, updatedAt):
    """Allow users to mark tasks in progress"""

    data = load_tasks()

    # CHEKC IF TASKS IS EMPTY
    if not data['tasks']:
        print("\n🔴 Error: The file is empty! Please enter a task first.")
        return
    
    for task in data['tasks']:
        if task['id'] == task_id:
            task['description'] = description
            task['status'] = "mark-in-progress"
            task['updatedAt'] = current_time()

            save_tasks(data)

            print(f"\n✅ Task successfully updated. \nTask ID: {task_id}")
            break
    else:
        print("\n❌ Task not found")


def main():
    
    # GREETING
    print("\n========== WELCOME ==========")

    parser = argparse.ArgumentParser(description='Simple Task Tracker CLI')
    subparsers = parser.add_subparsers(dest='command')

    # ADD COMMAND
    add_parser = subparsers.add_parser('add', help='Add new task')
    add_parser.add_argument('description', type=str, help='Task description')

    # UPDATE COMMAND
    update_parser = subparsers.add_parser('update', help='Update task')
    update_parser.add_argument('task_id', type=int, help='Task ID')
    update_parser.add_argument('description', type=str, help='New task description')

    # DELETE COMMAND
    delete_parser = subparsers.add_parser('delete', help='Delete task')
    delete_parser.add_argument('task_id', type=int, help='Task ID')

    # MARK IN PROGRESS COMMAND
    in_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark task in progress')
    in_progress_parser.add_argument('task_id', type=int, help='Task ID')

    # ROUTING LOGIC
    args = parser.parse_args()
    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'update':
        update_tasks(args.task_id, args.description)
    elif args.command == 'delete':
        delete_tasks(args.task_id)
    elif args.command == 'mark-in-progress':
        task_in_progress(args.task_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()