# Initial student data
students = [
    {"StudentID": 101, "Name": "Neha", "Age": 21, "Course": "AI"},
    {"StudentID": 102, "Name": "Arjun", "Age": 22, "Course": "ML"},
    {"StudentID": 103, "Name": "Sophia", "Age": 20, "Course": "Data Science"},
    {"StudentID": 104, "Name": "Ravi", "Age": 23, "Course": "AI"},
    {"StudentID": 105, "Name": "Meena", "Age": 21, "Course": "ML"},
]

# Insert new student
students.append({"StudentID": 106, "Name": "Amit", "Age": 22, "Course": "AI"})

# Update a course
for s in students:
    if s["StudentID"] == 102:
        s["Course"] = "AI"

# Delete a student
students = [s for s in students if s["StudentID"] != 104]

# Fetch students enrolled in "AI"
ai_students = [s for s in students if s["Course"] == "AI"]

print(ai_students)