# Task Tracker

A simple CLI app to track your tasks and manage your to-do list.


## Table of Contents
- [Feature Overview](#feature-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Usage Commands](#usage-commands)
- [Next Steps](#next-steps)


## Feature Overview
This program offers a comprehensive list of features to help you create, and manage your to-do list.

- `Add` Task: Allows you to add tasks to your to-do list app.
- `Update` Task: Allows you to update existing tasks.
- `Delete` Task: Allows you to delete tasks.
- `Mark Task as done`: Allows you to mark any given task as done.
- `Mark task in progress`: Allows you to mark any given task as in-progress.
- `List all tasks`: Allows you to list all the tasks in the program, regardless of status.
- `List done tasks`: Allows you to list all tasks marked as done.
- `List todo tasks`: Allows you to list all tasks marked as todo.
- `List in-progress tasks`: Allows you to list all tasks marked as in-progress.


## Installation
To install this program, use the command below:
```bash
- git clone https://github.com/fmax-dev/TASK-TRACKER.git

- cd TASK-TRACKER
```

## Usage
To start using this program:
1. Clone this repository using the commands above
2. Run `python task_tracker.py` on Windows or `python3 task_tracker.py` on Mac
3. Use any of the commands below to get started


## Usage Commands
Below is the list of commands and their usage to help you create and manage your tasks:

```bash
# Adding a new task
python task_tracker.py add "Buy groceries"

# Updating a task
python task_tracker.py update 1 "Buy groceries and cook dinner"

# Deleting a task
python task_tracker.py delete 1

# Marking a task as done
python task_tracker.py mark-done 1

# Marking a task as in progress
python task_tracker.py mark-in-progress 1

# Listing all tasks
python task_tracker.py list

# Listing done tasks
python task_tracker.py list done

# Listing todo tasks
python task_tracker.py list todo

# Listing in-progress tasks
python task_tracker.py list in-progress
```


## Next Steps
- Code Refactor
- Add due dates/deadlines for tasks
- Add priority levels (High, Medium, Low)
- Add task search functionality by keyword
- Implement SQLite database for better data persistence


## Project Source
This is a project from [Roadmap](https://roadmap.sh/). Click this [link](https://roadmap.sh/projects/task-tracker) to checkout the project.