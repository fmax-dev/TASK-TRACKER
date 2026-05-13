import os
import json
import argparse
from datetime import datetime


# JSON AS DB to store user tasks
TASKS_FILE = "task-tracker.json"

# AVAILABLE STATUS
VALID_STATUS = ["todo", "in-progress", "done"]

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
            break
    else:
        print(f"❌ No task found with ID: {task_id}")

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
        print(f"\n❌ No task found with ID: {task_id}")


def task_in_progress(task_id,):
    """Allow users to mark tasks in progress"""

    data = load_tasks()

    # CHEKC IF TASKS IS EMPTY
    if not data['tasks']:
        print("\n🔴 Error: The file is empty! Please enter a task first.")
        return
    
    for task in data['tasks']:
        if task['id'] == task_id:
            task['status'] = "in-progress"
            task['updatedAt'] = current_time()

            save_tasks(data)

            print(f"\n✅ Task successfully updated. \nTask ID: {task_id}")
            break
    else:
        print(f"\n❌ No task found with ID: {task_id}")


def mark_task_done(task_id):
    """Allow users to mark tasks as done"""

    data = load_tasks()

    # CHECK IF TASKS EMPTY
    if not data['tasks']:
        print("\n🔴 Error: The file is empty! Please enter a task first.")
        return
    
    for task in data['tasks']:
        if task['id'] == task_id:
            task['status'] = "done"
            task['updatedAt'] = current_time()

            save_tasks(data)

            print(f"\n✅ Task successfully updated. \nTask ID: {task_id}")
            break
    else:
        print(f"\n❌ No task found with ID: {task_id}")


def list_all_tasks():
    """Allow users to list all tasks regardless of their status"""

    data = load_tasks()

    # CHECK IF TASKS EMPTY
    if not data['tasks']:
        print("\n🔴 Error: The file is empty! Please enter a task first.")
        return
    
    print("\n========== ALL TASKS ==========\n")
    for index, task in enumerate(data['tasks'], start=1):
        print(f"{index}. Description: {task['description']} | ID: {task['id']} | Status: {task['status']}\n")
    

def list_tasks_by_status(status):
    """Allow users to list all tasks that are not done."""

    data = load_tasks()

    # CHECK IF TASKS EMPTY
    if not data['tasks']:
        print("\n🔴 Error: The file is empty! Please enter a task first.")
        return
    
    # CHECK IF VALID STATUS
    if status not in VALID_STATUS:
        print(f"\n🔴 Error: Please enter a valid status. \n{VALID_STATUS}")
        return
    
    # FILTER TASKS BY MATHCING STATUS
    filtered_tasks = []
    for task in data['tasks']:
        if task['status'] == status:
            filtered_tasks.append(task)

    # CHECK IF ANY TASKS WERE FOUND WITH STATUS
    if not filtered_tasks:
        print(f"\n🔴 No tasks found with status: {status}")
        return


    print(f"\n========== TASKS - {status.upper()} ==========\n")
    for index, task in enumerate(filtered_tasks, start=1):
        print(f"{index}. Description: {task['description']} | ID: {task['id']} | Status: {task['status']}\n")



def main():

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

    # MARK AS DONE COMMAND
    as_done_parser = subparsers.add_parser('mark-done', help='Mark tasks as done')
    as_done_parser.add_argument('task_id', type=int, help='Task ID')

    # LIST COMMANDS(HANDLES BOTH CASES)
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('status', nargs='?', default=None, help='Filter by status (to-do, in-progress, done)')
    

    # ROUTING LOGIC
    args = parser.parse_args()
    if args.command == 'add':
        add_task(args.description)
    # UPDATE COMMAND
    elif args.command == 'update':
        update_tasks(args.task_id, args.description)
    # DELETE COMMAND
    elif args.command == 'delete':
        delete_tasks(args.task_id)
    # MARK IN PROGRESS COMMAND
    elif args.command == 'mark-in-progress':
        task_in_progress(args.task_id)
    # MARK AS DONE COMMAND
    elif args.command == 'mark-done':
        mark_task_done(args.task_id)
    # LIST COMMANDS
    elif args.command == 'list':
        if args.status:
            list_tasks_by_status(args.status)
        else:
            list_all_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()