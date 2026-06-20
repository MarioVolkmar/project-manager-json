import os
from pprint import pprint

from storage import load_system, save_system
from members import (
    add_member,
    count_members_per_role,
    filter_members_by_role,
    filter_members_by_tasks_advance,
    count_member_tasks_by_status,
    count_member_tasks_by_priority,
    filter_members_by_tasks_priority,
    list_member_tasks,
)
from projects import (
    add_project,
    add_project_member,
    update_project_status,
    count_project_status,
    filter_project_status,
    list_projects,
)
from tasks import (
    create_task,
    assign_task,
    reassign_task,
    update_task_status,
    update_task_priority,
    update_task_hours,
    list_tasks,
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


# =========================
# CREAR MIEMBROS
# =========================
# Solo se crean si members.json está vacío.

add_member(members, "Mario Volkmar", "mario@email.com", "backend")
add_member(members, "Laura Gomez", "laura@email.com", "frontend")
add_member(members, "Carlos Perez", "carlos@email.com", "designer")
add_member(members, "Sofia Ramirez", "sofia@email.com", "qa")
add_member(members, "Andres Torres", "andres@email.com", "project_manager")


# =========================
# CREAR PROYECTOS
# =========================

add_project(
        projects,
        "Backend API",
        "API for managing members, projects and tasks",
    )
add_project(
        projects,
        "Ecommerce Automation",
        "Automation system for products, customers and sales",
    )

add_project(
        projects,
        "AI Support Assistant",
        "AI assistant for customer support workflows",
    )


# =========================
# AGREGAR MIEMBROS A PROYECTOS
# =========================


add_project_member(projects, members, 1, 1)
add_project_member(projects, members, 1, 2)
add_project_member(projects, members, 1, 4)
add_project_member(projects, members, 1, 5)

add_project_member(projects, members, 2, 1)
add_project_member(projects, members, 2, 3)
add_project_member(projects, members, 2, 5)

add_project_member(projects, members, 3, 1)
add_project_member(projects, members, 3, 2)
add_project_member(projects, members, 3, 4)
add_project_member(projects, members, 3, 5)


# =========================
# CREAR TAREAS
# =========================

create_task(
        tasks,
        projects,
        1,
        "Create project models",
        "Define base dictionaries for members, projects and tasks",
        "high",
        5,
    )

create_task(
        tasks,
        projects,
        1,
        "Build API endpoints",
        "Create CRUD endpoints for the backend API",
        "urgent",
        12,
    )

create_task(
        tasks,
        projects,
        1,
        "Test project workflow",
        "Validate project creation, updates and member assignment",
        "medium",
        4,
    )

create_task(
        tasks,
        projects,
        2,
        "Create product workflow",
        "Implement product creation and stock validation",
        "high",
        7,
    )

create_task(
        tasks,
        projects,
        2,
        "Design sales report",
        "Create basic sales summaries by customer and product",
        "medium",
        6,
    )

create_task(
        tasks,
        projects,
        3,
        "Prepare AI prompt logic",
        "Define prompt templates for support assistant responses",
        "high",
        8,
    )

create_task(
        tasks,
        projects,
        3,
        "Create QA test cases",
        "Prepare test cases for assistant answers and edge cases",
        "medium",
        5,
    )

create_task(
        tasks,
        projects,
        3,
        "Design assistant interface",
        "Create basic frontend structure for the assistant",
        "low",
        4,
    )
# =========================
# ASIGNAR TAREAS
# =========================

assign_task(members, 1, tasks, 1)
assign_task(members, 1, tasks, 2)
assign_task(members, 4, tasks, 3)

assign_task(members, 1, tasks, 4)
assign_task(members, 3, tasks, 5)

assign_task(members, 1, tasks, 6)
assign_task(members, 4, tasks, 7)
assign_task(members, 2, tasks, 8)

# =========================
# ACTUALIZAR TAREAS
# =========================

update_task_status(tasks, 1, "in_progress")
update_task_status(tasks, 3, "completed")
update_task_status(tasks, 5, "blocked")
update_task_status(tasks, 7, "in_progress")

update_task_priority(tasks, 8, "medium")
update_task_hours(tasks, 2, 15)

# =========================
# REASIGNAR TAREA
# =========================
# La tarea 8 estaba asignada a Laura.
# Ahora se reasigna a Mario.

reassign_task(members, 1, tasks, 8)


# =========================
# ACTUALIZAR ESTADO DE PROYECTOS
# =========================

update_project_status(projects, 1, "in_progress")
update_project_status(projects, 2, "in_progress")
update_project_status(projects, 3, "planning")


# =========================
# PRUEBAS DE VALIDACIÓN
# =========================

print("\n--- Intentos inválidos ---")

invalid_member = add_member(members, "Invalid User", "bad@email.com", "invalid_role")
print("Miembro con rol inválido:", invalid_member)

duplicated_member = add_member(members, "Mario Copy", "mario@email.com", "backend")
print("Miembro con email duplicado:", duplicated_member)

duplicated_project = add_project(projects, "Backend API", "Duplicated project")
print("Proyecto duplicado:", duplicated_project)

invalid_task = create_task(
    tasks,
    projects,
    99,
    "Invalid task",
    "Task for non-existing project",
    "high",
    3,
)
print("Tarea con proyecto inexistente:", invalid_task)

invalid_assignment = assign_task(members, 99, tasks, 1)
print("Asignación a miembro inexistente:", invalid_assignment)

duplicated_assignment = assign_task(members, 2, tasks, 1)
print("Asignación de tarea ya asignada:", duplicated_assignment)


# =========================
# REPORTES
# =========================

print("\n--- Miembros ---")
pprint(members)

print("\n--- Proyectos ---")
pprint(list_projects(projects))

print("\n--- Tareas ---")
pprint(list_tasks(tasks))

print("\n--- Tareas de Mario por ID ---")
pprint(list_member_tasks(members, 1))

print("\n--- Conteo de miembros por rol ---")
pprint(count_members_per_role(members))

print("\n--- Miembros agrupados por rol ---")
pprint(filter_members_by_role(members))

print("\n--- Avance de tareas por miembro ---")
pprint(filter_members_by_tasks_advance(members, tasks))

print("\n--- Conteo de tareas por estado por miembro ---")
pprint(count_member_tasks_by_status(members, tasks))

print("\n--- Conteo de tareas por prioridad por miembro ---")
pprint(count_member_tasks_by_priority(members, tasks))

print("\n--- Conteo global de tareas por prioridad desde miembros ---")
pprint(filter_members_by_tasks_priority(members, tasks))

print("\n--- Conteo de proyectos por estado ---")
pprint(count_project_status(projects))

print("\n--- Proyectos en progreso ---")
pprint(filter_project_status(projects, "in_progress"))


# =========================
# GUARDAR SISTEMA
# =========================

save_system(members, projects, tasks)

print("\nSistema guardado correctamente en data_files/")
