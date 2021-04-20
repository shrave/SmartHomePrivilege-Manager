#!/user/bin/env python

from app import create_app
from tests import test_app
from flask import jsonify
from flask import request
import json
import pickle
from task import task
from user import user

app = create_app()

with open('safety.pkl', 'rb') as input:
  safety_dict = pickle.load(input)

with open('task_objects.pkl', 'rb') as input:
  task_objects = pickle.load(input)

with open('user_list.pkl', 'rb') as file:
    user_list = pickle.load(file)


@app.route("/test", methods=["POST"])
def test():
  print(request.get_json(force = True))
  d = request.get_json(force = True)
  user_request_dict = json.loads(d)
  user_name = user_request_dict['User']
  task_name = user_request_dict['Task']
  #Get user object.
  for user in user_list:
    if user.name == user_name:
      user_object = user
  for task in task_objects:
    if task_name == task.name:
      print(task.privieges_allowed)
      user_privileges = task.validity_check(user_object)
  #Search the task directory, validate and 
  #get users eligible privieges using a function.
  # print(user_name, task_name)
  return user_privileges

if __name__ == '__main__':
  app.run()
