import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from recommender import get_project_recommendations
from chatbot import get_chat_response

app = FastAPI(title="ProjectMate: Internal Project Recommender")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("data.json", "r") as f:
    db = json.load(f)

@app.get("/")
def home():
    return {"message": "ProjectMate API is running 🚀"}

@app.get("/employees")
def list_employees():
    return db["employees"]

@app.post("/add_employee")
def add_employee(id: int, name: str, email: str, skills: str):
    # check if ID or email already exists
    for emp in db["employees"]:
        if emp["id"] == id:
            raise HTTPException(status_code=400, detail="Employee ID already exists.")
        if emp["email"].lower() == email.lower():
            raise HTTPException(status_code=400, detail="Email already exists.")

    new_emp = {
        "id": id,
        "name": name,
        "email": email,
        "skills": [s.strip() for s in skills.split(",")],
        "past_projects": []
    }
    db["employees"].append(new_emp)
    with open("data.json", "w") as f:
        json.dump(db, f, indent=4)
    return {"message": f"Employee {name} added successfully!"}

@app.get("/projects")
def list_projects():
    return db["projects"]

@app.get("/recommend/{employee_name}")
def recommend(employee_name: str):
    emp = next((e for e in db["employees"] if e["name"].lower() == employee_name.lower()), None)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return get_project_recommendations(emp["skills"], db["projects"])

@app.get("/chat/{message}")
def chat(message: str):
    response = get_chat_response(message)
    return {"reply": response}