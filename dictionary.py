# Dictionary Basics

student = {
    "name": "Niyati Jain",
    "age" : 20,
    "city": "Etah",
    "enrollment_no.": 141,
}

print(student["name"])
print(type(student))
print(student)
print(student["city"])
student["city"]= "Mumbai"
print(student)
student["favSubject"]= "python"
print(student)
student.pop("favSubject")
print(student)
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))

