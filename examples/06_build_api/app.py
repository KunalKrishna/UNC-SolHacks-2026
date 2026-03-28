"""
Task API — Exercise 06
=======================
Build a complete REST API for managing tasks. Complete each TODO with Copilot.

Run: uvicorn examples.06_build_api.app:app --reload
Docs: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException

# TODO: Import the models you defined in models.py
from .models import TaskStatus, TaskCreate, TaskUpdate, TaskResponse

app = FastAPI(
    title="Task Manager API",
    description="A simple task management API — built with GitHub Copilot!",
    version="1.0.0",
)

# In-memory storage (no database needed for this exercise)
tasks_db: dict[int, dict] = {}
next_id: int = 1


@app.get("/")
def root():
    """Health check endpoint."""
    return {"message": "Task Manager API is running!", "docs": "/docs"}


# ---------------------------------------------------------------------------
# TODO: Implement GET /tasks
# Return a list of all tasks.
# ---------------------------------------------------------------------------
@app.get("/tasks")
def get_tasks():
    return list(tasks_db.values())


# ---------------------------------------------------------------------------
# TODO: Implement GET /tasks/{task_id}
# Return a single task by ID.
# Raise HTTPException(status_code=404) if the task doesn't exist.
# ---------------------------------------------------------------------------
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# ---------------------------------------------------------------------------
# TODO: Implement POST /tasks
# Create a new task from a TaskCreate model.
# Assign it an auto-incrementing ID.
# Return the created task with status code 201.
# ---------------------------------------------------------------------------
@app.post("/tasks")
def create_task(task: TaskCreate):
    global next_id
    task_dict = task.dict()
    task_dict["id"] = next_id
    tasks_db[next_id] = task_dict
    next_id += 1
    return task_dict


# ---------------------------------------------------------------------------
# TODO: Implement PUT /tasks/{task_id}
# Update an existing task. Only update fields that are provided (not None).
# Raise HTTPException(status_code=404) if the task doesn't exist.
# Return the updated task.
# ---------------------------------------------------------------------------
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate): 
    existing_task = tasks_db.get(task_id)
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    update_data = task_update.dict(exclude_unset=True)
    existing_task.update(update_data)
    return existing_task

# ---------------------------------------------------------------------------
# TODO: Implement DELETE /tasks/{task_id}
# Delete a task by ID.
# Raise HTTPException(status_code=404) if the task doesn't exist.
# Return a confirmation message.
# ---------------------------------------------------------------------------
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks_db[task_id]
    return {"message": f"Task {task_id} deleted successfully."}