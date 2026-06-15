# Project Manager JSON

A console-based project and task management system built with Python.
This project simulates a simple project management workflow using projects, tasks, team members, task assignments, status updates, progress tracking, and JSON file persistence.

## Project Goal

The goal of this project is to practice Python fundamentals through a small real-world project management system.

This project focuses on:

* Modular programming
* Lists and dictionaries
* Data validation
* Relationships between entities
* Status management
* JSON persistence
* Basic business logic modeling

## Features

* Add and manage projects
* Add and manage team members
* Create tasks linked to projects
* Assign tasks to team members
* Update task status
* Filter tasks by project
* Filter tasks by member
* Filter tasks by status
* Calculate project progress
* Save and load data using JSON files

## Project Structure

```text
project-manager-json/
│
├── projects.py
├── members.py
├── tasks.py
├── storage.py
├── main.py
│
└── data_files/
    ├── projects.json
    ├── members.json
    └── tasks.json
```

## Modules

### `projects.py`

Contains the project logic:

* Add projects
* Search projects by ID
* Search projects by name
* Update project status
* Update project name
* Activate or deactivate projects
* List projects

### `members.py`

Contains the team member logic:

* Add members
* Search members by ID
* Search members by email
* Update member role
* Activate or deactivate members
* List members

### `tasks.py`

Contains the task logic:

* Add tasks
* Search tasks by ID
* Assign tasks to members
* Update task status
* Filter tasks by project
* Filter tasks by member
* Filter tasks by status
* Calculate project progress

### `storage.py`

Handles JSON persistence:

* Load data from JSON files
* Save data into JSON files
* Load the full system state
* Save the full system state

### `main.py`

Runs the full system workflow:

* Loads data
* Creates sample projects
* Creates sample members
* Creates sample tasks
* Assigns tasks to members
* Updates task statuses
* Calculates project progress
* Saves the updated data

## Data Models

### Project

```python
{
    "id_project": 1,
    "name": "Backend API",
    "description": "Build a basic backend API project",
    "status": "in_progress",
    "active": True
}
```

### Member

```python
{
    "id_member": 1,
    "name": "Mario Volkmar",
    "email": "mario@email.com",
    "role": "backend",
    "active": True
}
```

### Task

```python
{
    "id_task": 1,
    "project_id": 1,
    "title": "Create project structure",
    "description": "Create the base files and folders",
    "assigned_to": 1,
    "status": "completed",
    "priority": "high",
    "estimated_hours": 2,
    "active": True
}
```

## Suggested Status Values

### Project Status

```text
planning
in_progress
completed
cancelled
```

### Task Status

```text
pending
in_progress
completed
blocked
```

### Task Priority

```text
low
medium
high
urgent
```

## Business Rules

The system should validate that:

* Two projects cannot have the same name.
* Two members cannot have the same email.
* Tasks cannot be created for non-existing projects.
* Tasks cannot be assigned to non-existing members.
* Tasks cannot be assigned to inactive members.
* Invalid task statuses should not be allowed.
* Invalid project statuses should not be allowed.
* Project progress should be calculated based on completed tasks.

## Example Workflow

```text
1. Load projects, members, and tasks from JSON files.
2. Create projects.
3. Create team members.
4. Create tasks linked to projects.
5. Assign tasks to members.
6. Update task statuses.
7. Filter tasks by status, project, or member.
8. Calculate project progress.
9. Save the updated system data.
```

## Concepts Practiced

* Python functions
* Lists and dictionaries
* Modular programming
* JSON file handling
* Entity relationships
* Data validation
* Task assignment logic
* Status tracking
* Progress calculation
* Separation of responsibilities

## Current Status

This is a learning project created as part of my backend development training path.
The current version is designed as a console-based Python application using JSON files as simple local storage.

## Next Improvements

* Add automated tests
* Improve error messages
* Add a command-line menu
* Refactor repeated ID generation logic
* Add due dates for tasks
* Add task comments
* Add project reports
* Later migrate the project to FastAPI and PostgreSQL

## Author

Created by Mario Volkmar as part of a backend development learning roadmap.
