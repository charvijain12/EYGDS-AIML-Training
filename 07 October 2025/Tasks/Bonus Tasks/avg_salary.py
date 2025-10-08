@app.get("/employees/average-salary")
def average_salary():
    if not employees:
        return {"average_salary": 0}
    avg = sum(emp["salary"] for emp in employees) / len(employees)
    return {"average_salary": round(avg, 2)}