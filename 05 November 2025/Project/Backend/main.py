from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import Employee, Project
from recommender import get_project_recommendations
from chatbot import get_chat_response
import json

# -------------------------------------------------------------------
# 🌟 FastAPI App Initialization
# -------------------------------------------------------------------
app = FastAPI(title="ProjectMate Backend", version="1.0")

# -------------------------------------------------------------------
# 🧱 Database Setup
# -------------------------------------------------------------------
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------------------------------------------------
# 🌍 CORS Configuration (Frontend Access)
# -------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify e.g., ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------------------
# 🏠 Root Endpoint
# -------------------------------------------------------------------
@app.get("/")
def home():
    return {"message": "ProjectMate API is live 🚀"}


# -------------------------------------------------------------------
# 👥 Employee Endpoints
# -------------------------------------------------------------------

# Get all employees
@app.get("/api/employees")
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return employees


# Add new employee
@app.post("/api/employees")
def add_employee(
    id: int,
    name: str,
    email: str,
    skills: str,
    db: Session = Depends(get_db)
):
    # Check duplicates
    if db.query(Employee).filter(Employee.id == id).first():
        raise HTTPException(status_code=400, detail="Employee ID already exists.")
    if db.query(Employee).filter(Employee.email == email).first():
        raise HTTPException(status_code=400, detail="Email already exists.")

    new_emp = Employee(
        id=id,
        name=name,
        email=email,
        skills=[s.strip().lower() for s in skills.split(",")],
        past_projects=[]
    )
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return {"message": f"Employee {name} added successfully!"}


# -------------------------------------------------------------------
# 📋 Projects & Recommendations
# -------------------------------------------------------------------

# Load all projects from JSON file
@app.get("/api/projects")
def get_projects():
    with open("data/projects.json", "r") as f:
        return json.load(f)


# Recommend projects based on skills
@app.get("/api/employees/{name}/recommendations")
def recommend(name: str, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.name.ilike(name)).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    with open("data/projects.json", "r") as f:
        projects = json.load(f)

    recommendations = get_project_recommendations(emp.skills, projects)
    return {
        "employee": emp.name,
        "recommendations": recommendations
    }


# -------------------------------------------------------------------
# 💬 Chatbot Endpoint
# -------------------------------------------------------------------
@app.post("/api/chat")
def chat(message: str):
    response = get_chat_response(message)
    return {"reply": response}


# -------------------------------------------------------------------
# 📡 Run Check
# -------------------------------------------------------------------
@app.get("/api/status")
def status():
    return {"status": "ok", "message": "Backend is healthy ✅"}
