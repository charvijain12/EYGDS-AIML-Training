from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    StudentID: int
    Name: str
    Age: int
    Course: str

students_db = []

@app.get("/students")
def get_students():
    return students_db

@app.post("/students")
def add_student(student: Student):
    students_db.append(student)
    return {"message": "Student added"}

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for idx, s in enumerate(students_db):
        if s.StudentID == student_id:
            students_db[idx] = student
            return {"message": "Student updated"}
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for idx, s in enumerate(students_db):
        if s.StudentID == student_id:
            del students_db[idx]
            return {"message": "Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found")
