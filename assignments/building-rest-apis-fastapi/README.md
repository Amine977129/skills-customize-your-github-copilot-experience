# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing tasks with FastAPI. Practice defining routes, using HTTP methods and status codes, validating request data with Pydantic models, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create the API and Add Tasks

#### Description

Complete the starter code to create a FastAPI application for a task list. Add endpoints to view all tasks and create a task, using an in-memory collection so no database setup is needed.

#### Requirements

Completed program should:

- Install FastAPI and Uvicorn with `python -m pip install fastapi uvicorn`.
- Create a FastAPI application that can be run with `uvicorn main:app --reload`.
- Define a Pydantic model that requires a non-empty task title and allows a task to be marked as complete.
- Return the task list as JSON from `GET /tasks` with a `200` status code.
- Accept a task title at `POST /tasks`, assign it a unique integer ID, store it, and return the created task with a `201` status code.
- Let FastAPI return a validation error for a request with a missing or invalid title.

### 🛠️ Read, Update, and Delete Tasks

#### Description

Add endpoints for working with one task at a time. Use the task ID from the URL to find the task and return a clear not-found response when it does not exist.

#### Requirements

Completed program should:

- Return one task from `GET /tasks/{task_id}` with a `200` status code.
- Update a task from `PATCH /tasks/{task_id}` using only the fields supplied in the request, and return the updated task with a `200` status code.
- Delete a task from `DELETE /tasks/{task_id}` and return a `204` status code when deletion succeeds.
- Return a `404` status code with a helpful detail message when a requested task ID does not exist.
