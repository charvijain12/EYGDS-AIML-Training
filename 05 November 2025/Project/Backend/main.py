# main.py
from fastapi import FastAPI, HTTPException, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db
from models import Employee, Project

app = FastAPI(title="ProjectMate API")

# Allow frontend (local or deployed)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "🚀 ProjectMate API running successfully!"}

# -------------------- EMPLOYEES --------------------

@app.post("/api/employees")
def add_employee(employee: dict = Body(...), db: Session = Depends(get_db)):
    existing = db.query(Employee).filter(Employee.email == employee["email"]).first()
    if existing:
        raise HTTPException(status_code=400, detail="Employee already exists")
    
    new_emp = Employee(
        name=employee["name"],
        email=employee["email"],
        password=employee["password"],
        skills=employee.get("skills", []),
        past_projects=employee.get("past_projects", [])
    )

    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return {"message": f"Employee '{new_emp.name}' added successfully!", "id": new_emp.id}


@app.get("/api/employees")
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return [
        {
            "id": e.id,
            "name": e.name,
            "email": e.email,
            "skills": e.skills,
            "past_projects": e.past_projects
        }
        for e in employees
    ]

# -------------------- LOGIN --------------------

@app.post("/api/login")
def login(data: dict = Body(...), db: Session = Depends(get_db)):
    user = db.query(Employee).filter(Employee.email == data["email"]).first()
    if not user or user.password != data["password"]:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"message": f"Welcome {user.name}!", "id": user.id}

# -------------------- PROJECTS --------------------

@app.post("/api/projects")
def add_project(project: dict = Body(...), db: Session = Depends(get_db)):
    new_proj = Project(
        name=project["name"],
        description=project["description"],
        required_skills=project.get("required_skills", []),
        status=project.get("status", "open")
    )
    db.add(new_proj)
    db.commit()
    db.refresh(new_proj)
    return {"message": f"Project '{new_proj.name}' added successfully!"}


@app.get("/api/projects")
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    return [
        {
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "required_skills": p.required_skills,
            "status": p.status
        }
        for p in projects
    ]


@app.get("/api/recommend/{employee_name}")
def recommend(employee_name: str, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.name == employee_name).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    projects = db.query(Project).filter(Project.status == "open").all()
    recs = []
    for p in projects:
        overlap = len(set(emp.skills or []) & set(p.required_skills or []))
        match = round((overlap / len(p.required_skills)) * 100, 2) if p.required_skills else 0
        recs.append({
            "project": p.name,
            "description": p.description,
            "match_score": match
        })
    recs.sort(key=lambda x: x["match_score"], reverse=True)
    return {"employee": employee_name, "recommendations": recs}