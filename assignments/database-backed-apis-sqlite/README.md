# 📘 Assignment: Database-Backed APIs with SQLite

## 🎯 Objective

Extend a FastAPI task API to store tasks in an SQLite database instead of temporary in-memory data. Practice creating a database table, running parameterized SQL queries, and connecting REST endpoints to persistent records.

## 📝 Tasks

### 🛠️ Create the Database and Persist Tasks

#### Description

Use Python's built-in `sqlite3` module to create a database file and a `tasks` table. Update the task-list and task-creation endpoints so they read and write records in SQLite.

#### Requirements

Completed program should:

- Install FastAPI and Uvicorn with `python -m pip install fastapi uvicorn`; use Python's built-in `sqlite3` module without installing a database package.
- Create a `tasks` table with an integer primary key, a required title, and a completed field when the application starts.
- Return stored tasks as JSON from `GET /tasks`.
- Save a task sent to `POST /tasks` and return its database-generated ID and fields with a `201` status code.
- Use SQL parameters rather than building SQL statements by inserting user-provided values into query strings.

### 🛠️ Connect CRUD Endpoints to SQLite

#### Description

Replace the remaining in-memory behavior with database queries so that retrieving, updating, and deleting tasks all use SQLite records.

#### Requirements

Completed program should:

- Retrieve a task by ID from `GET /tasks/{task_id}` and return a `404` status code if it does not exist.
- Update only the fields supplied to `PATCH /tasks/{task_id}` and return the updated task.
- Delete a task with `DELETE /tasks/{task_id}`, returning a `204` status code when successful and `404` when the task does not exist.
- Close database connections after each operation.
- Keep created tasks available after stopping and restarting the FastAPI server.
