#normal py class

class Student:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email

#valid data
data = {"name":"Ali","age":"twenty","email":"ali@example.com"}
student = Student(**data)

print(student.age)

