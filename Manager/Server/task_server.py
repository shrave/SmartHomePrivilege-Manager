#!/user/bin/env python

from app import create_app
from tests import test_app
from flask import jsonify
from flask import request
import json
import pickle
import threading

from flask import Flask
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Krsna_12'
app.config['MYSQL_DATABASE_DB'] = 'smarthomes'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

app = create_app()

with open('../../safety.pkl', 'rb') as input:
	safety_dict = pickle.load(input)

with open('../../task_objects.pkl', 'rb') as input:
	task_objects = pickle.load(input)

with open('../../user_list.pkl', 'rb') as file:
	user_list = pickle.load(file)

with open('../../devices.pkl', 'rb') as file:
	device_list = pickle.load(file)

def commit_job_ends(user_privileges):
	for device in user_privileges:
		for privilege in user_privileges[device]:
			print(privilege, device)
			cursor.execute("INSERT INTO Resource_ownership (Owner, Task, Device, Privilege, Timestamp,  Status) VALUES ('System', 'End Task', '%s'   , '%s'    , CURRENT_TIME() , 'Available');",(device,privilege))
			cursor.commit()
			resource_master_list[(device, privilege)] = 'available'
			#commit privilege, device mysql unoccupied command.

def initial_resource_status():
	#make all resources to availble and commit.
	resource_master_list = {}
	for device in device_list:
		for privilege in device_list[device]:
			resource_master_list[(device, privilege)] = 'available'
			cursor.execute("INSERT INTO Resource_ownership (Owner, Task, Device, Privilege, Timestamp,  Status) VALUES ('System', 'Initial', '%s'   , '%s'    , CURRENT_TIME() , 'Available');",(device,privilege))
			cursor.commit()

@app.route("/test", methods=["POST"])
def test():
	user_privileges = {}
	print(request.get_json(force = True))
	d = request.get_json(force = True)
	ip_addr = request.remote_addr
	# print(ip_addr)
	# now = datetime.now()
	# formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
	user_request_dict = json.loads(d)
	user_name = user_request_dict['User']
	task_name = user_request_dict['Task']
	#Record the request and its response in the table.
	conn = mysql.connect()
	cursor =conn.cursor()
	#Get user object.
	user_object = []
	for user in user_list:
		if user.Name == user_name:
			user_object = user
	if not user_object:
		print("User not registered in the house.")
		# INSERT INTO API_Request(User, Task, Timestamp, Validity, Status, ip_address, Message, Resources_allowed) VALUES('krsna', 'Cook Food', CURRENT_TIME() ,
		#0, 'Failed',  INET_ATON('127.0.0.1'),'User not registered in the house.','None');
		cursor.execute("INSERT INTO API_Request (User, Task, Timestamp, Validity, Status, ip_address, Message, Resources_allowed) VALUES (%s, %s, CURRENT_TIME(), 0, 'Failed',  INET_ATON(%s),'User not registered in the house.','None');",(user_name, task_name,ip_addr))
		conn.commit()
		return {"System response":"User not registered in the house."}
	for task in task_objects:
		if task_name == task.name:
			# print(task.name)
			# print(task.privileges_allowed)
			# print(task.validity_check(user_object))
			# print(dir(task))
			time = task.time
			print(time)
			user_privileges = task.validity_check(user_object)
	#Search the task directory, validate and 
	#get users eligible privieges using a function.
	# print(user_name, task_name)
	# print(user_privileges)
	if not user_privileges:
		cursor.execute("INSERT INTO API_Request (User, Task, Timestamp, Validity, Status, ip_address, Message, Resources_allowed) VALUES (%s, %s, CURRENT_TIME(), 0, 'Failed',  INET_ATON(%s),'Task not defined by home owner.','None');",(user_name, task_name,ip_addr))
		conn.commit()
		return {"System response":"Task not defined by home owner."}
	cursor.execute("INSERT INTO API_Request (User, Task, Timestamp, Validity, Status, ip_address, Message, Resources_allowed) VALUES (%s, %s, CURRENT_TIME(), %s, 'Success',  INET_ATON(%s),'User has been given privileges of the task.',%s);",(user_name, task_name, str(time),ip_addr, json.dumps(user_privileges)))
	#Loop through all resources in each device and commit them.
		for device in user_privileges:
			for privilege in user_privileges[device]:
				if resource_master_list[(device, privilege)] == 'available':
					print(privilege, device)
					cursor.execute("INSERT INTO Resource_ownership (Owner, Task, Device, Privilege, Timestamp,  Status) VALUES ('%s', '%s', '%s'   , '%s'    , CURRENT_TIME() , 'Available');",(user_name, task_name,device,privilege))
					cursor.commit()
					resource_master_list[(device, privilege)] = 'occupied'
	threading.timer(time, commit_job_ends, ['user_privileges'])
	return user_privileges

if __name__ == '__main__':
	app.run()
