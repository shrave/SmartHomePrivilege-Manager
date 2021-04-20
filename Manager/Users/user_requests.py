import json
import requests

user_name = input ("Enter name of the user :")

task_name = input("Enter task requested : ")

print(user_name+' requesting to perform '+task_name + ' task...')
user_request_dict = {
    "User": user_name,
    "Task": task_name
}
jsonData = json.dumps(user_request_dict)

response = requests.post('http://127.0.0.1:5000/test', json=jsonData)

print("Status code: ", response.status_code)
print("Printing Entire Post Request")
print(response.json())