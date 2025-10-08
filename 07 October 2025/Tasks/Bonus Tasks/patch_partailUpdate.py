from typing import Optional

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[float] = None

@app.patch("/employees/{emp_id}")
def partial_update(emp_id: int, update_data: EmployeeUpdate):
    for emp in employees:
        if emp["id"] == emp_id:
            if update_data.name is not None:
                emp["name"] = update_data.name
            if update_data.department is not None:
                emp["department"] = update_data.department
            if update_data.salary is not None:
                emp["salary"] = update_data.salary
            return {"message": "Employee partially updated", "employee": emp}
    raise HTTPException(status_code=404, detail="Employee not found")