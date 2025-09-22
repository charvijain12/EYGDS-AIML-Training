#dictionary uses curly brackets
#adding and updating data is possible
# dict is mutable
student = {
    "name" : "Charvi",
    "age" : 22,
    "course" : "AI & ML"
}
print(student["name"]) #access by key
print(student.get("age"))

student["grade"]="A" #adding new key-value
student["age"]="23" #updating existing field

#any of the below two can be used for removing/deleting key-values
student.pop("course") #remove by key (more method way)
del student["grade"] #delete key (more function way)

#iteration
for key, value in student.items():
    print(key, ":" ,value)

print(student)

#nested data in dictionary
student["skills"]=["Python","C++","Java","Excel"]
print(student["skills"][1]) #accessing nested data

