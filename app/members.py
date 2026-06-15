from utils import normalize_text, next_id

ALLOWED_ROLES = ["backend" , "frontend" , "designer" , "qa" , "project_manager"]

def add_member(members, name, email, role):
    if normalize_text(role) not in ALLOWED_ROLES:
        return None
    
    src = search_member_by_email(members, email)
    if src is not None:
        return None
    
    id_member = next_id(members, "id_member")

    member ={
        "id_member" : id_member,
        "name" : normalize_text(name),
        "email" : normalize_text(email),
        "role" : normalize_text(role),
        "active" : True, 
        "tasks" : []
    }

    members.append(member)
    return member

def search_member_by_id(members, id_member):
    for m in members:
        if m["id_member"] == id_member:
            return m
    return None

def search_member_by_email(members, email):
    for m in members:
        if normalize_text(m["email"]) == normalize_text(email):
            return m
    return None

def update_member_email(members, id_member, email):
    src_id = search_member_by_id(members, id_member)
    if src_id is None:
        return None
    src_email = search_member_by_email(members, email)
    if src_email is not None:
        return None
    src_id["email"] = normalize_text(email)
    return src_id

def update_member_role(members, id_member, role):
    if normalize_text(role) not in ALLOWED_ROLES:
        return None
    
    src = search_member_by_id(members, id_member)
    if src is None:
        return None
    src["role"] = normalize_text(role)
    return src

def update_member_status(members,id_member):
    src = search_member_by_id(members, id_member)
    if src is None:
        return None
    src["active"] = not src["active"]
    return src

def filter_members_by_role(members):
    res = {}
    for m in members:
        role = normalize_text(m["role"])
        if role not in res:
            res[role] = []
        res[role].append(m)
    return res

def count_members_per_role(members):
    res = {}
    for m in members:
        role = normalize_text(m["role"])
        if role not in res:
            res[role] = 0
        res[role] += 1
    return res

def filter_members_by_tasks_advance(members):
    res = {
        "no_tasks" : 0,
        "pending_some_task" : 0,
        "complete_all_tasks" : 0
    }
    for m in members:
        if len(m["tasks"]) == 0:
            res["no_tasks"] += 1
        else:
            for t in m["tasks"]:
                if normalize_text(t["status"]) != "completed":
                    res["pending_some_task"] += 1
                    break
            else:
                res["complete_all_tasks"] += 1   
    return res

def count_member_tasks_by_status(members):
    res = []
    for m in members:
        tasks = {
            "id_member" : m["id_member"]
        }
        for t in m["tasks"]:
            name = normalize_text(t["status"])
            if name not in tasks:
                tasks[name] = 0
            tasks[name] += 1
        res.append(tasks)
    return res

def list_members(members):
    return members

