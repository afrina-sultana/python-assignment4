import json

student = {
    "name": "Afrina Sultana",
    "age": 20,
    "department": "CSE"
}

json_data = json.dumps(student)
print(json_data)