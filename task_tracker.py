import os
import json
import argparse
from datetime import datetime


# JSON AS DB to store user tasks
TASKS_FILE = "task-tracker.json"

# AVAILABLE STATUS
VALID_STATUS = ["to-do", "in-progress", "done"]

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
        return json.dump(data, file, indent=4)
        

def add_task(description):
    """Add tasks to file"""
    data = load_tasks()

    # GENERATING TASK ID
    data["last_id"] += 1
    task_id = data["last_id"]

    timestamp = datetime.now().isoformat()

    # CREATING TASK FIELD
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



def main():
    
    # GREETING
    print("\n========== WELCOME ==========")

    parser = argparse.ArgumentParser(description='Simple Task Tracker CLI')
    subparsers = parser.add_subparsers(dest='command')

    # ADD COMMAND
    add_parser = subparsers.add_parser('add', help='Add new task')
    add_parser.add_argument('description', type=str, help='Task description')


    args = parser.parse_args()
    if args.command == 'add':
        add_task(args.description)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()