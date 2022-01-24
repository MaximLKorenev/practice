import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(response.text)

with open("file.json", "w") as json_file:
    json.dump(result, json_file)

n = len(result)
user_id = result[0]['userId']
count_user = 1
num = 0
completed = 0
id = 0
user = {}

for i in range(n):

    if result[i]['userId'] != user_id:
        user[result[i-1]["userId"]] = {"num": num, "completed": completed}
        num = 0
        completed = 0
        count_user += 1
        user_id = result[i]['userId']

    if result[i]['id'] != id:
        num += 1

    if result[i]["completed"]:
        completed += 1

    if i == n - 1:
        user[result[i]["userId"]] = {"num": num, "completed": completed}

