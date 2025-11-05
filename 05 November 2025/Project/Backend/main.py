from fastapi import FastAPI, HTTPException
from recommender import get_project_recommendations
from chatbot import get_chat_response

app = FastAPI(title="Internal Project Matching Chatbot")

# Sample in-memory data
employees = {
    "charvi": {"skills": ["python", "data analysis", "flask", "sql"]}
}

projects = [
    {"name": "Customer Insights Dashboard", "skills": ["python", "sql", "tableau"]},
    {"name": "Chatbot HR Assistant", "skills": ["nlp", "python", "flask"]},
    {"name": "Automation Script Tool", "skills": ["python", "selenium"]},
]

@app.get("/")
def home():
    return {"message": "Internal Project Matching API is running"}

@app.get("/recommend/{employee_name}")
def recommend(employee_name: str):
    if employee_name not in employees:
        raise HTTPException(status_code=404, detail="Employee not found")
    emp_skills = employees[employee_name]["skills"]
    return get_project_recommendations(emp_skills, projects)

@app.post("/chat")
def chat(message: str):
    response = get_chat_response(message)
    return {"reply": response}