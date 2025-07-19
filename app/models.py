from pydantic import BaseModel

# Model input dari client (POST request)
class TodoCreate(BaseModel):
    title: str
    description: str
    completed: bool = False

# Model output yang dikembalikan ke client
class Todo(TodoCreate):
    id: int