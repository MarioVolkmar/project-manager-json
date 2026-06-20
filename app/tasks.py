from members import search_member_by_id
from projects import search_project_by_id
from utils import normalize_text, next_id


ALLOWED_STATUS = ["pending", "in_progress", "completed" ,"blocked"]
ALLOWED_PRIORITIES = ["low", "medium", "high", "urgent"]

def create_task(tasks, projects, id_project, title, description, priority, estimated_hours):
    title = normalize_text(title)
    description = normalize_text(description)
    priority = normalize_text(priority)

    if priority not in ALLOWED_PRIORITIES or estimated_hours <= 0:
        return None

    src_project = search_project_by_id(projects  , id_project)
    if src_project  is None:
        return None
    
    n_id = next_id(tasks,"id_task")

    task ={
    "id_task": n_id,
    "project_id": id_project,
    "title": title,
    "description": description,
    "status": "pending",
    "priority": priority,
    "estimated_hours": estimated_hours,
    "assigned_to": None,
    "active": True
    }
    tasks.append(task)
    return task
    

def search_task_by_id(tasks, id_task):
    for t in tasks:
        if t["id_task"] == id_task:
            return t
    return None

def search_task_by_title(tasks, title):
    title = normalize_text(title)
    for t in tasks:
        if t["title"] == title:
            return t
    return None

def assign_task(members, id_member, tasks, id_task):
    src_m = search_member_by_id(members, id_member)
    task = search_task_by_id(tasks, id_task)
    
    if src_m is None or task is None or task["assigned_to"] is not None or src_m["active"] is False:
        return None

    src_m["tasks"].append(task["id_task"])
    task["assigned_to"] = id_member
    return task

def update_task_priority(tasks, id_task, priority):
    priority = normalize_text(priority)

    if priority not in ALLOWED_PRIORITIES:
        return None
    
    task = search_task_by_id(tasks, id_task)
    if task is None:
        return None
    task["priority"] = priority
    return task

def update_task_status(tasks, id_task, status):
    status = normalize_text(status)

    if status not in ALLOWED_STATUS:
        return None
    
    task = search_task_by_id(tasks, id_task)
    if task is None:
        return None
    task["status"] = status
    return task

def update_task_title(tasks, id_task, title):
    title = normalize_text(title)
    task = search_task_by_id(tasks, id_task)
    if task is None:
        return None
    task["title"] = title
    return task

def update_task_description(tasks, id_task, description):
    description = normalize_text(description)
    task = search_task_by_id(tasks, id_task)
    if task is None:
        return None
    task["description"] = description
    return task

def update_task_hours(tasks, id_task, hours):
    if hours <= 0:
        return None
    task = search_task_by_id(tasks, id_task)
    if task is None:
        return None
    task["estimated_hours"] = hours
    return task

def update_task_active(tasks, id_task):
    task = search_task_by_id(tasks, id_task)
    if task is None:
        return None
    task["active"] = not task["active"]
    return task


def reassign_task(members, id_member, tasks, id_task):
    member = search_member_by_id(members, id_member)
    task = search_task_by_id(tasks, id_task)
    
    if member is None or task is None or task["assigned_to"] is None or member["active"] is False:
        return None
    
    id_member_actual = task["assigned_to"]

    if id_member_actual == id_member:
        return None
    
    member["tasks"].append(task["id_task"])
    task["assigned_to"] = id_member
    member_actual = search_member_by_id(members, id_member_actual)
    member_actual["tasks"].remove(id_task)

    return task
    
def list_tasks(tasks):
    return tasks