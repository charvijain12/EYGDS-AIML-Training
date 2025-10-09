from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend (HTML/React/Angular) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to specific URLs in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple GET API that returns 5 students
@app.get("/students")
def get_students():
    students = [
        {"id": 1, "name": "Alice", "grade": "A"},
        {"id": 2, "name": "Bob", "grade": "B"},
        {"id": 3, "name": "Charlie", "grade": "A"},
        {"id": 4, "name": "Diana", "grade": "C"},
        {"id": 5, "name": "Evan", "grade": "B"},
    ]
    return {"students": students}
    
    
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Students List</title>
</head>
<body>
  <h2>Students</h2>
  <button onclick="loadStudents()">Load Students</button>
  <ul id="studentList"></ul>

  <script>
    async function loadStudents() {
      const response = await fetch("http://127.0.0.1:8000/students");
      const data = await response.json();
      const students = data.students;

      const list = document.getElementById("studentList");
      list.innerHTML = ""; // clear old list

      students.forEach(s => {
        const item = document.createElement("li");
        item.textContent = `${s.name} (Grade: ${s.grade})`;
        list.appendChild(item);
      });
    }
  </script>
</body>
</html>
