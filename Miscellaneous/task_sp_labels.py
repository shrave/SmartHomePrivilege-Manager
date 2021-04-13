import pandas as pd
import pickle

#Retrieving previous device instances based on current floorplan.
with open('../safety.pkl', 'rb') as input:
    safety_dict = pickle.load(input)

df = pd.read_excel('Tasks.xlsx')

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
device_acronym_list = []
for k in task_dict.keys():
	# print(k)
	# print(task_dict[k])
	for j in task_dict[k].keys():
		# print(j)
		# print(task_dict[k][j])
		for l in task_dict[k][j].keys():
			# print(l)
			device_acronym_list.append(l)
			# print(task_dict[k][j][l])
			# for i in task_dict[k][j][l]:
			# 	print(i)
	# 			print(safety_dict[l[0]][i])
			# print('\n')
		# print('\n')
	# print('\n')
# print(task_dict)
# print(device_acronym_list)
with open('../device_label.pkl', 'rb') as input:
	device_master_list = pickle.load(input)
with open('../devices_floorplan.pkl', 'rb') as input:
	device_list = pickle.load(input)
# print(device_master_list)
device_master_list['Motion sensors only'] = ['MF1','MF2','MF5','MF7','MF9','MF10']
device_master_list['L1-6'] = device_master_list['Smart Light']
device_master_list['Thermo1-2,4-5'] = device_master_list['Thermostat'].remove('Thermo3')
device_master_list['L1-2'] = ['L1', 'L2']
device_master_list['MF'] = device_master_list['Contact and flame sensors']
device_master_list['S'] = device_master_list['Smart shower']
device_master_list['P'] = device_master_list['Smart Plug/Socket']
device_master_list['Light'] = device_master_list['Smart Light']
device_master_list['ALL'] = device_master_list['Smart Plug/Socket']
device_master_list['Thermo1-5'] = device_master_list['Thermostat']
device_master_list['echo'] = ['Echo']
for tup in device_acronym_list:
	print('**********')
	# print(tup)
	# print(device_master_list[tup[0]])
	if tup[1] not in device_master_list[tup[0]]:
		# print(tup)
		# print(device_master_list[tup[0]])
		if tup[1] not in device_master_list:
			print(tup)
			print(device_master_list[tup[0]])
		# if ('In their device owned rooms only' or 'respective')== tup[1]:
		# 	for device in device_list:
		# 		if task.location == device.location:
		# 			if device.name == tup[0]:
		# 				print(device)

