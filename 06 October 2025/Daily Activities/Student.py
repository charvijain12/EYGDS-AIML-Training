from pydantic import BaseModel

#define a model
class Student(BaseModel):
    name: str
    age: int
    email: str
    is_active: bool = True

#valid data
data = {"name":"Aisha","age":21,"email":"aisha@example.com"}
student = Student(**data)

print(student)
print(student.name)