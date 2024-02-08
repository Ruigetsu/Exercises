import json
users = {
    "name": "Ivan", 
    "surname": "Drago",
    "email": "IvanDrago@mail.ru"
}

json_data = json.dumps(users)

print(json_data)

data = json.loads(json_data)

print(data['name'])