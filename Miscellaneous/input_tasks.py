import pandas as pd

df = pd.read_excel('Tasks.xlsx')
tasks = df['Task Name']
device_name = df['Device Name']
users = df['User']
privileges = df['Privileges']
labels = df['Label']

#Divide into blocks.
g = []
blocks = []
for j,k,l,m,n in zip(tasks,privileges, device_name, users,  labels):
	if str(j)!='nan': #new task
		blocks.append(g)
		g = []
		g.append((str(j),str(k),str(l),str(m),str(n)))
	else:
		g.append((str(j),str(k),str(l),str(m),str(n)))
blocks.append(g)
blocks = list(filter(None, blocks)) 
tasks={}
for k in blocks:
	for i in k:
		#check if task is present.
		if (i[0] not in tasks.keys()) and (i[0] != 'nan'):
			tasks[i[0]] = {}
		#check if devce is present.
		if tuple(i[3].split(',')) not in tasks[i[0]].keys():
			tasks[i[0]][tuple(i[3].split(','))] = {}
			print(i[3].split(','))
		if (i[2],tuple(i[4].split(','))) not in tasks[i[0]][tuple(i[3].split(','))].keys():
			tasks[i[0]][tuple(i[3].split(','))][(i[2],tuple(i[4].split(',')))] = [i[1]]
		else:
			tasks[i[0]][tuple(i[3].split(','))][(i[2],tuple(i[4].split(',')))].append(i[1])

# for k in tasks['Throw a party']:
# 	print(k)
# 	for i in tasks['Throw a party'][k]:
# 		print((i, tasks['Throw a party'][k][i]))
# 	print('\n')
print(tasks)
#Task dictionary has the following format:
#{Task Name: {users allowed: {(Device name, label): [Privileges list]}}}
#ALL consists of all the labels-> meaning all devices.
#respective or location means those devices in the same location.