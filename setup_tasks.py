import pandas as pd
import pickle
from task import task
def save_object(obj, filename):
	with open(filename, 'wb') as output:  # Overwrites any existing file.
		pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
#Retrieving previous device instances based on current floorplan.
with open('safety.pkl', 'rb') as input:
    safety_dict = pickle.load(input)

print(safety_dict)
df = pd.read_excel('Miscellaneous/Tasks.xlsx')

df = df.dropna(	)
task_dict = {}
tasks = df['Task Name']
device_name = df['Device Name']
users = df['User']
#change users' format.
user_list = []
for k in users:
	j = k.split(',')
	temp = []
	for i in j:
		temp.append(i[-1])
	user_list.append(tuple(temp))
# print(user_list)
users = user_list
privileges = df['Privileges']
labels = df['Label']
#{Task Name: {users allowed: {(Device name, label): [Privileges list]}}}
#ALL consists of all the labels-> meaning all devices.
#respective or location means those devices in the same location.
for j,k,l,m,n in zip(tasks, users, device_name,labels,privileges):
	if j not in task_dict.keys():
		task_dict[j] = {}
	if k not in task_dict[j].keys():
		task_dict[j][k] = {}
	if (l,m) not in task_dict[j][k].keys():
		task_dict[j][k][(l,m)] = [n]
	else:
		task_dict[j][k][(l,m)].append(n)

# print(task_dict)
task_acronym_list = []
for k in task_dict.keys():
	# print(k)
	# print(task_dict[k])
	for j in task_dict[k].keys():
		# print(j)
		# print(task_dict[k][j])
		for l in task_dict[k][j].keys():
			# print(l)
			task_acronym_list.append(l)
			# print(task_dict[k][j][l])
			# for i in task_dict[k][j][l]:
				# print(i)
	# 			print(safety_dict[l[0]][i])
			# print('\n')
		# print('\n')
	# print('\n')
# print(task_dict)
# print(task_acronym_list)
with open('device_label.pkl', 'rb') as input:
	device_master_list = pickle.load(input)
with open('devices_floorplan.pkl', 'rb') as input:
	device_list = pickle.load(input)
# print(device_master_list)
device_master_list['Motion sensors only'] = ['MF1','MF2','MF5','MF7','MF9','MF10']
device_master_list['L1-6'] = device_master_list['Smart Light']
device_master_list['Thermo1-2,4-5'] = device_master_list['Thermostat'][:-1]
device_master_list['L1-2'] = ['L1', 'L2']
device_master_list['MF'] = device_master_list['Contact and flame sensors']
device_master_list['S'] = device_master_list['Smart shower']
device_master_list['P'] = device_master_list['Smart Plug/Socket']
device_master_list['Light'] = device_master_list['Smart Light']
device_master_list['ALL'] = device_master_list['Smart Plug/Socket']
device_master_list['Thermo1-5'] = device_master_list['Thermostat']
device_master_list['echo'] = ['Echo']


def retrieve_object(label):
	for device in device_list:
		if device.label == label:
			return device
#Mapping device objects to task definitions.
# for tup in task_acronym_list:
	# print('**********')
	# print(tup)
	# print(tup)
	# print(device_master_list[tup[0]])
	# if tup[1] in device_master_list[tup[0]]:
		# print(tup[1])
		# print(device_master_list[tup[0]])
	# if tup[1] in device_master_list:
		# print(tup[1])
		# print(device_master_list[tup[1]])
	# print('*********')
		# if tup[1] not in device_master_list:
			# print(tup)
			# print(device_master_list[tup[0]])
			# pass
		# if ('In their device owned rooms only' or 'respective')== tup[1]:
		# 	for device in device_list:
		# 		if task.location == device.location:
		# 			if device.name == tup[0]:
		# 				print(device)
task_object_lists = []
for k in task_dict.keys():
	print(k)
	# print(task_dict[k])
	users_devices = {}
	for j in task_dict[k].keys():
		# print(j)
		# print(task_dict[k][j])
		device_privileges = {}
		for l in task_dict[k][j].keys():
			if l[1] in device_master_list:
				# print(device_master_list[l[1]])
				for label in device_master_list[l[1]]:
					# device_objects.append(retrieve_object(label))
					privis = retrieve_object(label)
					# print(privis)
					if privis not in device_privileges:
						device_privileges[privis] = []
					# print(privis.privileges)
					for i in task_dict[k][j][l]:
						# print(i)
						if i in privis.privileges:
							device_privileges[privis].append(i)
				#Get the devices from the function.
				#Put it to the task and privileges.
				#Load the task.
				#Finally at runtime- ask for the location, time
				#Accept the requests and test.
				# for i in task_dict[k][j][l]:
					# print(i)
			if l[1] in device_master_list[l[0]]:
				# print(device_master_list[l[0]])
				# print(l[1])
				for label in device_master_list[l[0]]:
					# device_objects.append(retrieve_object(label))
					privis = retrieve_object(label)
					if privis not in device_privileges:
						device_privileges[privis] = []
					# print(privis.privileges)
					for i in task_dict[k][j][l]:
						# print(i)
						if i in privis.privileges:
							device_privileges[privis].append(i)
		# print(device_privileges)
		users_devices[j] = device_privileges
	# print(users_devices)
	only_privileges = {}
	for jrm in users_devices:
		for key in users_devices[jrm]:
			if key not in only_privileges:
				only_privileges[key] = users_devices[jrm][key]
			else:
				only_privileges[key].extend(users_devices[jrm][key])
	task_privileges_dict = {}
	for jj in only_privileges:
		# print(len(only_privileges[jj]))
		task_privileges_dict[jj] = list(set(only_privileges[jj]))
		# print(len(task_privileges_dict[jj]))
		# print('***')
	print(task_privileges_dict)
	# print(only_privileges)
	task_object_lists.append(task(k,task_privileges_dict))

# print(task_object_lists)
for ta in task_object_lists:
	print(dir(ta))
	print(ta.name)
	# print(task.privileges_allowed)
# save_object(task_object_lists, 'task_objects.pkl')
