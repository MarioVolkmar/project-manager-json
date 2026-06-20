import os
from pprint import pprint

from storage import load_system, save_system
from members import (
    add_member,
    count_members_per_role,
    filter_members_by_tasks_advance,
    count_member_tasks_by_status,
    count_member_tasks_by_priority,
    filter_members_by_tasks_priority,
    list_members,
    search_member_by_id,
    ALLOWED_ROLES
)
from projects import (
    add_project,
    add_project_member,
    count_project_status,
    filter_project_status,
    list_projects,
    search_project_by_id
)
from tasks import (
    create_task,
    assign_task,
    reassign_task,
    update_task_status,
    list_tasks,
    search_task_by_id,
    ALLOWED_PRIORITIES,
    ALLOWED_STATUS
)


# =========================
# PREPARAR ARCHIVOS
# =========================

os.makedirs("data_files", exist_ok=True)


# =========================
# CARGAR SISTEMA
# =========================
# Este main carga los datos existentes desde JSON.

members, projects, tasks = load_system()

while True:
    s = input("1. List members 2. Add member 3. List projects 4. Add project 5. Add member to project 6. List tasks 7. Create task 8. Assign task 9. Update task status 10. Show reports 0. Save and exit ")
    if s == "0":
        print("Informacion guardada")
        save_system(members,projects,tasks)
        break
    elif s == "1":
        pprint(list_members(members))
    elif s == "2":
        name = input("Name: ")
        email = input("Email: ")
        while True:
            possible_roles = ["1","2","3","4","5"]
            role = input("1. Backend 2. Frontend 3. Designer 4. QA 5. Project_manager")
            if role not in possible_roles:
                print("Invalid input")
            else:
                role_index = int(role) - 1
                role = ALLOWED_ROLES[role_index]
                break
        member = add_member(members, name, email, role)
        if member is None:
            print("Email is already in use")
        else:    
            pprint(f"Member: \n{member}")
    elif s == "3":
        pprint(list_projects(projects))
    elif s == "4":
        name = input("Name: ")
        description = input("Description: ")
        project = add_project(projects, name, description)
        if project is None:
            print("The project name is in use")
        else:
            pprint(f"Project: \n{project}")
    elif s == "5":
        member_id = input("Id member: ")
        project_id = input("Id project ")
        try:
            member_id = int(member_id)
        except ValueError:
            print("Invalid id member")
            continue
        try:
            project_id = int(project_id)
        except ValueError:
            print("Invalid id project")
            continue
        member = search_member_by_id(members, member_id)
        project = search_project_by_id(projects, project_id)
        if member is None:
            print("Member does not exist")
        elif project is None:
            print("Project does not exist")
        elif  not member["active"]:
            print("Member inactive")
        elif not project["active"]:
            print("Project inactive")
        else:
            member_add = add_project_member(projects, members, project_id, member_id)
            if member_add is None:
                print("This member is already assigned to this project")
            else:
                pprint(f"Project: \n{member_add}")
    elif s == "6":
        pprint(list_tasks(tasks))
    elif s == "7":
        project_id = input("Project Id: ")
        try:
            project_id = int(project_id)
        except ValueError:
            print("Invalid id project")
            continue
        project = search_project_by_id(projects, project_id)

        if project is None:
            print("Project does not exist")
            continue

        if not project["active"]:
            print("Project is inactive")
            continue

        title = input("Title: ")
        description = input("Description: ")
        while True:
            estimated_hours = input("Estimated hours: ")
            try:
                estimated_hours = float(estimated_hours)
                if estimated_hours <= 0:
                    print("The hours must be higher than 0")
                else:
                    break
            except ValueError:
                print("Invalid input")
        while True:
            priority = input("1. Low 2. Medium 3. High 4. Urgent ")
            possible_priority = ["1","2","3","4"]
            if priority not in possible_priority:
                print("Invalid input")
            else:
                priority_index = int(priority) - 1
                priority = ALLOWED_PRIORITIES[priority_index]
                break
        task = create_task(tasks, projects, project_id, title, description, priority, estimated_hours)
        pprint(f"Task: \n{task}")
    elif s == "8":
        member_id = input("Member id: ")
        try:
            member_id = int(member_id)
        except ValueError:
            print("Invalid input")
            continue
        task_id = input("Task id: ")
        try:
            task_id = int(task_id)
        except ValueError:
            print("Invalid input")
            continue
        task = search_task_by_id(tasks, task_id)
        if task is None:
            print("Task does not exist")
            continue
        if  not task["active"]:
            print("Task is inactive")
            continue
        member = search_member_by_id(members, member_id)
        if member is None:
            print("Member does not exist")
            continue
        if not member["active"]:
            print("Member is inactive")
            continue
        if task_id in member["tasks"]:
            print("Task is already assigned to this member")
            continue
        
        if task["assigned_to"] is not None:
            re_task = reassign_task(members, member_id, tasks, task_id)
            pprint(f"Task: \n{re_task}")
        else:
            re_task = assign_task(members, member_id, tasks, task_id)
            pprint(f"Task: \n{re_task}")
    elif s == "9":
        task_id = input("Id Task: ")
        try:
            task_id = int(task_id)
        except ValueError:
            print("Invalid id task")
            continue
        while True:
            status = input("1. Pending 2. In progress 3. Completed 4. Blocked")
            possible_status = ["1","2","3","4"]
            if status not in possible_status:
                print("Invalid input")
            else:
                status_index = int(status) - 1
                status = ALLOWED_STATUS[status_index]
                break
        src_task = search_task_by_id(tasks, task_id)
        if src_task is None:
            print("Task does not exist")
            continue
        if  not src_task["active"]:
            print("Task is inactive")
            continue
        task = update_task_status(tasks, task_id, status)
        pprint(f"Task: \n{task}")
    elif s == "10":
        while True:
            sr = input("1. Member count by role 2. Project count by status 3. Task progress by members 4. Tasks by status by member 5. Tasks by priority by member 6. Overall priority count 7. Projects in progress 0. Exit")
            if sr == "0":
                break
            elif sr == "1":
                pprint(count_members_per_role(members))
            elif sr == "2":
                pprint(count_project_status(projects))
            elif sr == "3":
                pprint(filter_members_by_tasks_advance(members, tasks))
            elif sr == "4":
                pprint(count_member_tasks_by_status(members, tasks))
            elif sr == "5":
                pprint(count_member_tasks_by_priority(members,tasks))
            elif sr == "6":
                pprint(filter_members_by_tasks_priority(members, tasks))
            elif sr == "7":
                pprint(filter_project_status(projects,"in_progress"))
            else:
                print("Invalid input")
    else:
        print("Invalid input")
