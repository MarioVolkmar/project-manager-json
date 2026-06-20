ALLOWED_PROJECT_STATUS = ["planning", "in_progress", "completed", "cancelled"]
from utils import normalize_text, next_id
from members import search_member_by_id

def add_project (projects, name, description, status = "planning"):
    name = normalize_text(name)
    description = normalize_text(description)
    status = normalize_text(status)

    if status not in ALLOWED_PROJECT_STATUS:
        return None
    
    src = search_project_by_name(projects, name)
    if src is not None:
        return None
    
    id_project = next_id(projects, "id_project")

    project = {
        "id_project" : id_project,
        "name" : name,
        "description" : description,
        "status" : status,
        "active" : True,
        "members" : []
    }
    projects.append(project)
    return project


def search_project_by_name(projects, name):
    name = normalize_text(name)
    for p in projects:
        if normalize_text(p["name"]) == name:
            return p
    return None

def search_project_by_id (projects, id_project):
    for p in projects:
        if p["id_project"] == id_project:
            return p
    return None

def update_project_name (projects, id_project, name):
    name = normalize_text(name)
    src_id = search_project_by_id(projects, id_project)
    if src_id is None:
        return None
    src_name = search_project_by_name(projects, name)
    if src_name is not None:
        return None
    src_id["name"] = name
    return src_id

def update_project_description (projects, id_project, description):
    description = normalize_text(description)
    src = search_project_by_id(projects, id_project)
    if src is None:
        return None
    src["description"] = description
    return src

def update_project_status (projects, id_project, status):
    status = normalize_text(status)
    if status not in ALLOWED_PROJECT_STATUS:
        return None
    src = search_project_by_id(projects, id_project)
    if src is None:
        return None
    src["status"] = status
    return src

def update_project_active (projects, id_project):
    src = search_project_by_id(projects, id_project)
    if src is None:
        return None
    src["active"] = not src["active"]
    if src["active"]:
        src["status"] = ALLOWED_PROJECT_STATUS[1]
    else:
        src["status"] = ALLOWED_PROJECT_STATUS[-1]
    return src

def add_project_member (projects, members, id_project, id_member):
    src_project = search_project_by_id (projects, id_project)
    src_member = search_member_by_id (members, id_member)
    if src_member is None or src_project is None:
        return None
    if id_member in src_project["members"] or not src_member["active"]:
        return None
    src_project["members"].append(id_member)
    return src_project

def remove_project_member (projects, members, id_project, id_member):
    src_project = search_project_by_id (projects, id_project)
    src_member = search_member_by_id (members, id_member)
    if src_member is None or src_project is None:
        return None
    if id_member not in src_project["members"]:
        return None
    src_project["members"].remove(id_member)
    return src_project

def count_project_status (projects):
    res = {}
    for p in projects:
        if p["status"] not in res:
            res[p["status"]] = 0
        res[p["status"]] += 1
    return res

def filter_project_status (projects, status):
    status = normalize_text(status)

    if status not in ALLOWED_PROJECT_STATUS:
        return None
    
    res = []

    for p in projects:
        if p["status"] == status:
            res.append(p)

    return res

def list_projects (projects):
    return projects