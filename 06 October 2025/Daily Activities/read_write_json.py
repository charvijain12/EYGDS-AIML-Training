import json

student={
    "name":"Vikram",
    "age":22,
    "courses":["AI","ML"],
    "marks":{"AI":89,"ML":90}
}

#write to a json file
with open("student.json",'w') as f:
    json.dump(student,f,indent=4)

#read from json file
with open("student.json",'r') as f:
    data = json.load(f)

print(data["name"])  #vikram will be printed
print(data["marks"]["AI"]) #89