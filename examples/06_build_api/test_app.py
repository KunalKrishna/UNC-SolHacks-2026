"""
Tests for the Task API — Exercise 06

These tests verify the API endpoints. Complete the TODOs or let Copilot
generate tests by asking: "Generate tests for the Task Manager API."

Run: pytest examples/06_build_api/test_app.py -v
"""

import pytest
from fastapi.testclient import TestClient

# NOTE: These tests will only work after you complete models.py and app.py.
# Uncomment the imports below once your API is implemented.

import app
client = TestClient(app.app)


# ---------------------------------------------------------------------------
# TODO: Test the health check endpoint
# GET / should return status 200 and a message
# ---------------------------------------------------------------------------
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Task Manager API is running!", "docs": "/docs"}

# ---------------------------------------------------------------------------
# TODO: Test creating a task
# POST /tasks with a title should return status 201
# The response should include an id, title, description, and status
# ---------------------------------------------------------------------------
def test_create_task():
    task_data = {"title": "Test Task"}
    response = client.post("/tasks", json=task_data)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["title"] == "Test Task"
    assert data["description"] == ""
    assert data["status"] == "todo"

# ---------------------------------------------------------------------------
# TODO: Test getting all tasks
# After creating a task, GET /tasks should return a list containing it
# ---------------------------------------------------------------------------
def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# ---------------------------------------------------------------------------
# TODO: Test getting a single task
# After creating a task, GET /tasks/{id} should return that task
# ---------------------------------------------------------------------------
def test_get_task():    
    # First create a task to ensure it exists
    task_data = {"title": "Another Test Task"}
    create_response = client.post("/tasks", json=task_data)
    task_id = create_response.json()["id"]

    # Now get the task by ID
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == "Another Test Task"

# ---------------------------------------------------------------------------
# TODO: Test getting a non-existent task
# GET /tasks/999 should return status 404
# ---------------------------------------------------------------------------
def test_get_non_existent_task():
    response = client.get("/tasks/999")
    assert response.status_code == 404

# ---------------------------------------------------------------------------
# TODO: Test updating a task
# PUT /tasks/{id} with new data should update and return the task
# ---------------------------------------------------------------------------
def test_update_task():
    # First create a task to update
    task_data = {"title": "Task to Update"}
    create_response = client.post("/tasks", json=task_data)
    task_id = create_response.json()["id"]

    # Now update the task
    update_data = {"title": "Updated Task Title", "status": "in_progress"}
    response = client.put(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == "Updated Task Title"
    assert data["status"] == "in_progress"

# ---------------------------------------------------------------------------
# TODO: Test deleting a task
# DELETE /tasks/{id} should return status 200
# GET /tasks/{id} after deletion should return 404
# ---------------------------------------------------------------------------
def test_delete_task():
    # First create a task to delete
    task_data = {"title": "Task to Delete"}
    create_response = client.post("/tasks", json=task_data)
    task_id = create_response.json()["id"]

    # Now delete the task
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200

    # Verify the task is deleted
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404