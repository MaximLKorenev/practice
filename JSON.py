import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(response.text)

with open("file.json", "w") as json_file:
    json.dump(result, json_file)

users = {}
for user in result:
    user_id = user["userId"]
    if user_id not in users:
        users[user_id] = {"num": 0, "completed": 0}
    users[user_id]["num"] += 1
    if user["completed"]:
        users[user_id]["completed"] += 1

print(users)
