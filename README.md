
# Robot Management API (FastAPI)

This is a simple REST API for registering robots, updating their status,
retrieving robot information, and storing activity logs.

## Features

- Register robots with ID, name, type, and status
- Update robot status (battery, location, mode, error)
- Get all robots / get one robot
- Create and fetch robot activity logs
- Proper error handling with HTTP status codes

## How to Run

1. Create and activate a virtual environment (optional but recommended).

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the FastAPI server from the project root:

```bash
uvicorn app.main:app --reload
```

4. Open the interactive API docs in your browser:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Example Endpoints

- `POST /robots` - register a new robot
- `PUT /robots/{robot_id}/status` - update robot status
- `GET /robots` - list all robots
- `GET /robots/{robot_id}` - get a single robot
- `POST /robots/{robot_id}/logs` - add a log entry
- `GET /robots/{robot_id}/logs` - view robot logs

This project is intentionally simple and uses in-memory storage, so it is
easy to understand and extend with a real database (SQLite/MySQL/MongoDB)
and authentication (JWT) if needed.
