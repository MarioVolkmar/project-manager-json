import json
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        return [] 
    elif os.path.getsize(file_path) == 0:
        return []
    with open(file_path, "r" , encoding="utf-8") as file:
        return json.load(file)
    
def save_data(file_path, data):
    with open(file_path, "w" , encoding="utf-8") as file:
        json.dump(data, file, indent= 4, ensure_ascii = False)

def load_system():
    members = load_data("data_files/members.json")
    projects = load_data("data_files/projects.json")
    tasks = load_data("data_files/tasks.json")
    return members, projects, tasks

def save_system(members, projects, tasks):
    save_data("data_files/members.json", members)
    save_data("data_files/projects.json", projects)
    save_data("data_files/tasks.json", tasks)