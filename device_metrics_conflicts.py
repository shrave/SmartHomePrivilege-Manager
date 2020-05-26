import pickle
from itertools import combinations
import pandas as pd 

#Function for pickling variables.
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

#Retrieving previous device instances based on current floorplan.
with open('devices.pkl', 'rb') as input:
    device_instances = pickle.load(input)

df = pd.read_excel('Device_security.xlsx')
# print(df.to_dict(orient='dict'))
df = df.dropna(	)
safety_dict = {}
for j,k,l in zip(df['Device Name'], df['Functionality'], df['Critical Tags']):
	if j not in safety_dict.keys():
		safety_dict[j] = {}
	if k not in safety_dict[j].keys():
		safety_dict[j][k] = l
# print(safety_dict)
save_object(safety_dict, 'safety.pkl')
for k in safety_dict.keys():
	print(k)
	for l in safety_dict[k].keys():
		print(l)
		print(safety_dict[k][l])
	print('\n')
user_metric_privilege = {}
user_metric_security = {}
for k in device_instances:
	# print(k.name)
	user_metric_privilege[k.name] = {}
	user_metric_security[k.name] = {}
	for i in range(1,7): 
		# print('User number '+str(i))
		user_metric_privilege[k.name][i] = set()
		user_metric_security[k.name][i] = set()
		for l in k.user_groups.keys():
			if i in k.user_groups[l]:
				#here l is a privilege and i is a user number denoting a user group.
				try:
					# print((k.name, l, 'pass'))
					user_metric_privilege[k.name][i].add((l,safety_dict[k.name][l]))
					user_metric_security[k.name][i].add(safety_dict[k.name][l])
				except Exception as e:
					# print((k.name, l, 'fail'))
					pass
				
		# print('\n')
	# print('\n')

# for k in user_metric_security:
# 	print(k)
# 	for j in user_metric_privilege[k]:
# 		print(j)
# 		for i in user_metric_privilege[k][j]:
# 			print(i)
# 		print('\n')
# 	print('\n')