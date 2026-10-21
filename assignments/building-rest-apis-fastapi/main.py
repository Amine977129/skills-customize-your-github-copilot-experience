from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1)
    completed: bool | None = None


# Store tasks in memory. They reset whenever the server restarts.
tasks: dict[int, dict] = {}
next_task_id = 1


@app.get("/tasks")
def list_tasks():
    # TODO: Return all tasks.
    pass


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    # TODO: Assign a unique ID, save the task, and return it.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Return the task, or raise HTTPException with status 404.
    pass


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, changes: TaskUpdate):
    # TODO: Update only supplied fields and return the task.
    pass


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    # TODO: Delete the task, or raise HTTPException with status 404.
    pass
