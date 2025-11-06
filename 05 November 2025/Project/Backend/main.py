# main.py
from fastapi import FastAPI, HTTPException, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db
from models import Employee, Project
import json

app = FastAPI(title="ProjectMate API - Internal Recommender")

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"] for tighter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def home():
    return {"message": "🚀 ProjectMate API is running successfully!"}


# -----------------------------
# Add New Employee
# -----------------------------
@app.post("/api/employees")
def add_employee(employee: dict = Body(...), db: Session = Depends(get_db)):
    # Check if user already exists
    existing = db.query(Employee).filter(Employee.email == employee["email"]).first()
    if existing:
        raise HTTPException(status_code=400, detail="Employee already exists")

    new_emp = Employee(
        name=employee["name"],
        email=employee["email"],
        password=employee["password"],  # stored as plain text for now (hash later)
        skills=json.dumps(employee.get("skills", []))
    )

    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)

    return {"message": f"Employee '{new_emp.name}' added successfully!", "id": new_emp.id}


# -----------------------------
# Get All Employees
# -----------------------------
@app.get("/api/employees")
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    result = []
    for e in employees:
        result.append({
            "id": e.id,
            "name": e.name,
            "email": e.email,
            "skills": json.loads(e.skills) if e.skills else []
        })
    return result


# -----------------------------
# Employee Login
# -----------------------------
@app.post("/api/login")
def login(data: dict = Body(...), db: Session = Depends(get_db)):
    user = db.query(Employee).filter(Employee.email == data["email"]).first()
    if not user or user.password != data["password"]:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"message": f"Welcome {user.name}!", "id": user.id}


# -----------------------------
# Get All Projects
# -----------------------------
@app.get("/api/projects")
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    result = []
    for p in projects:
        result.append({
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "required_skills": p.required_skills.split(","),
            "status": p.status
        })
    return result


# -----------------------------
# Recommend Projects for an Employee
# -----------------------------
@app.get("/api/recommend/{employee_name}")
def recommend_projects(employee_name: str, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.name == employee_name).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    employee_skills = json.loads(employee.skills)
    projects = db.query(Project).filter(Project.status == "open").all()

    recommendations = []
    for p in projects:
        project_skills = [s.strip().lower() for s in p.required_skills.split(",")]
        common = len(set(employee_skills) & set(project_skills))
        match_score = round((common / len(project_skills)) * 100, 2) if project_skills else 0

        recommendations.append({
            "project_name": p.name,
            "description": p.description,
            "match_score": match_score
        })

    recommendations.sort(key=lambda x: x["match_score"], reverse=True)
    return {"employee": employee_name, "recommendations": recommendations}


# -----------------------------
# Health Check Endpoint
# -----------------------------
@app.get("/api/status")
def status():
    return {"status": "ok"}