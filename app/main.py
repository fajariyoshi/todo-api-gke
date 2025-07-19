from fastapi import FastAPI
from app.models import Todo, TodoCreate
from typing import List

app = FastAPI()
todos: List[Todo] = []
id_counter = 1  # simple id generator

@app.get("/")
def root():
    return {"message": "OK"}

@app.get("/todos", response_model=List[Todo])
def get_all_todos():
    return todos

@app.post("/todos", response_model=Todo)
def add_todo(todo_data: TodoCreate):
    global id_counter
    todo = Todo(id=id_counter, **todo_data.dict())
    id_counter += 1
    todos.append(todo)
    return todo