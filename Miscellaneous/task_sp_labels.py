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
for k in task_dict.keys():
	# print(k)
	for j in task_dict[k].keys():
		print(j)
		for l in task_dict[k][j].keys():
			print(l)
			for i in task_dict[k][j][l]:
				# print(i)
				print(safety_dict[l[0]][i], end='<')
			print('\n')
		print('\n')
	# print('\n')

