from fastapi.testclient import TestClient
from app.main import app
from app.models import Todo

client = TestClient(app)

def test_get_all_todos_initially_empty():
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []

def test_add_todo():
    new_todo = {
        "id": 1,
        "title": "Belajar CI/CD",
        "description": "Pahami dasar CI/CD pipeline dengan GitHub Actions",
        "completed": False
    }
    response = client.post("/todos", json=new_todo)
    assert response.status_code == 200
    assert response.json() == new_todo

def test_get_all_todos_after_post():
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) >= 1  # Minimal 1 karena sebelumnya kita POST
