"""country = {
    "name": "America",
    "Location": "South",
    "Population": "300 Million",
    "Sports": ["Football", "Volleyball", "Cricket"]
}
print(country)
country.popitem()
del country["name"]"""


# create dictionary
student = {
    "name": "Sushant",
    "age": 20,
    "course": "BCSIT"
}

# print dictionary
print(student)

# access values
print(student["name"])
print(student["age"])

# add new item
student["city"] = "Kathmandu"

# update value
student["age"] = 21

# print updated dictionary
print(student)

# remove item
student.pop("course")

# print after removal
print(student)

# dictionary length
print(len(student))

# loop through dictionary
for key, value in student.items():
    print(key, ":", value)

# check key exists
if "name" in student:
    print("Name exists")

# copy dictionary
new_student = student.copy()

# print copied dictionary
print(new_student)

# nested dictionary
students = {
    "student1": {
        "name": "Ram",
        "age": 19
    },
    "student2": {
        "name": "Shyam",
        "age": 20
    }
}

# print nested dictionary
print(students)

# access nested value
print(students["student1"]["name"])

# dictionary methods
print(student.keys())
print(student.values())
print(student.items())