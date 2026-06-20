from utils import normalize_text, next_id, search_by_id

ALLOWED_ROLES = ["backend" , "frontend" , "designer" , "qa" , "project_manager"]

def add_member(members, name, email, role):
    name = normalize_text(name)
    email = normalize_text(email)
    role = normalize_text(role)

    if role not in ALLOWED_ROLES:
        return None
    
    src = search_member_by_email(members, email)
    if src is not None:
        return None
    
    id_member = next_id(members, "id_member")

    member ={
        "id_member" : id_member,
        "name" : name,
        "email" : email,
        "role" : role,
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
    email = normalize_text(email)
    for m in members:
        if normalize_text(m["email"]) == email:
            return m
    return None

def update_member_email(members, id_member, email):
    email = normalize_text(email)
    src_id = search_member_by_id(members, id_member)
    if src_id is None:
        return None
    src_email = search_member_by_email(members, email)
    if src_email is not None:
        return None
    src_id["email"] = email
    return src_id

def update_member_role(members, id_member, role):
    role = normalize_text(role)
    if role not in ALLOWED_ROLES:
        return None
    
    src = search_member_by_id(members, id_member)
    if src is None:
        return None
    src["role"] = role
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

def filter_members_by_tasks_advance(members, tasks):
    res = {
        "no_tasks" : 0,
        "pending_some_task" : 0,
        "complete_all_tasks" : 0
    }
    for m in members:
        if len(m["tasks"]) == 0:
            res["no_tasks"] += 1
        else:
            for task in m["tasks"]:
                t = search_by_id(tasks,"id_task", task)
                if normalize_text(t["status"]) != "completed":
                    res["pending_some_task"] += 1
                    break
            else:
                res["complete_all_tasks"] += 1   
    return res

def count_member_tasks_by_status(members, task_list):
    res = []
    for m in members:
        tasks = {
            "id_member" : m["id_member"]
        }
        for task in m["tasks"]:
            t = search_by_id(task_list ,"id_task", task)
            name = normalize_text(t["status"])
            if name not in tasks:
                tasks[name] = 0
            tasks[name] += 1
        res.append(tasks)
    return res

def count_member_tasks_by_priority(members, task_list):
    res = []
    for m in members:
        tasks = {
            "id_member" : m["id_member"]
        }
        for task in m["tasks"]:
            t = search_by_id(task_list,"id_task", task)
            name = normalize_text(t["priority"])
            if name not in tasks:
                tasks[name] = 0
            tasks[name] += 1
        res.append(tasks)
    return res

def filter_members_by_tasks_priority(members, tasks):
    res = {}
    for m in members:
            for task in m["tasks"]:
                t = search_by_id(tasks,"id_task", task)
                if normalize_text(t["priority"]) not in res:
                    res[normalize_text(t["priority"]) ] = 0
                res[normalize_text(t["priority"]) ] += 1 
    return res


def list_member_tasks(members, id_member):
    src = search_member_by_id(members,id_member) 
    if src is None:
        return None
    return src["tasks"]

def list_members(members):
    return members