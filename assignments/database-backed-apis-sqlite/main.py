import sqlite3
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()
DATABASE_PATH = Path(__file__).with_name("tasks.db")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1)
    completed: bool | None = None


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database() -> None:
    connection = get_connection()
    try:
        # TODO: Create the tasks table if it does not already exist.
        pass
    finally:
        connection.close()


initialize_database()


@app.get("/tasks")
def list_tasks():
    # TODO: Read all tasks from SQLite and return them as dictionaries.
    pass


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    # TODO: Insert a task using SQL parameters and return its generated ID.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Query SQLite for this task; raise HTTPException with status 404 if absent.
    pass


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, changes: TaskUpdate):
    # TODO: Update only supplied fields; raise HTTPException with status 404 if absent.
    pass


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    # TODO: Delete this task; raise HTTPException with status 404 if absent.
    pass
