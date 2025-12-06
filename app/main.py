
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict

app = FastAPI(title="Robot Management API", version="1.0.0")

# In-memory storage for demo purposes
robots: Dict[str, dict] = {}
logs: Dict[str, list] = {}

class Robot(BaseModel):
    id: str
    name: str
    type: str
    status: str  # e.g. "idle", "active", "charging", "error"

class StatusUpdate(BaseModel):
    battery: Optional[int] = None  # percentage
    location: Optional[str] = None
    mode: Optional[str] = None     # idle, charging, active
    error: Optional[str] = None

class LogEntry(BaseModel):
    message: str

@app.post("/robots")
def create_robot(robot: Robot):
    """Register a new robot with id, name, type, status."""
    if robot.id in robots:
        raise HTTPException(status_code=400, detail="Robot already exists")
    robots[robot.id] = {
        **robot.dict(),
        "battery": None,
        "location": None,
        "mode": None,
        "error": None,
    }
    logs[robot.id] = []
    return {"message": "Robot created", "robot": robots[robot.id]}

@app.put("/robots/{robot_id}/status")
def update_status(robot_id: str, status: StatusUpdate):
    """Update robot's battery, location, mode or error state."""
    if robot_id not in robots:
        raise HTTPException(status_code=404, detail="Robot not found")
    # Only update fields that are provided
    for key, value in status.dict().items():
        if value is not None:
            robots[robot_id][key] = value
    return {"message": "Status updated", "robot": robots[robot_id]}

@app.get("/robots")
def get_robots():
    """Get list of all robots."""
    return list(robots.values())

@app.get("/robots/{robot_id}")
def get_robot(robot_id: str):
    """Get details of a specific robot."""
    if robot_id not in robots:
        raise HTTPException(status_code=404, detail="Robot not found")
    return robots[robot_id]

@app.post("/robots/{robot_id}/logs")
def create_log(robot_id: str, log: LogEntry):
    """Create a log entry for a robot."""
    if robot_id not in robots:
        raise HTTPException(status_code=404, detail="Robot not found")
    logs[robot_id].append(log.message)
    return {"message": "Log added"}

@app.get("/robots/{robot_id}/logs")
def get_logs(robot_id: str):
    """Retrieve all logs for a robot."""
    if robot_id not in robots:
        raise HTTPException(status_code=404, detail="Robot not found")
    return {"robot_id": robot_id, "logs": logs[robot_id]}

# Simple health check
@app.get("/health")
def health():
    return {"status": "ok"}
