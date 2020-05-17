import pickle
from itertools import combinations
import pandas as pd 
#Retrieving previous device instances based on current floorplan.
with open('devices.pkl', 'rb') as input:
    device_instances = pickle.load(input)

for k in device_instances:
	if k.name == 'Amazon Echo':
		print(k.user_groups)
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

# for k in safety_dict.keys():
# 	print(k)
# 	for l in safety_dict[k].keys():
# 		print(l)
# 		print(safety_dict[k][l])
# 	print('\n')
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
				
				try:
					# print((k.name, l, 'pass'))
					user_metric_privilege[k.name][i].add((l,safety_dict[k.name][l]))
					user_metric_security[k.name][i].add(safety_dict[k.name][l])
				except Exception as e:
					# print((k.name, l, 'fail'))
					pass
				
		# print('\n')
	# print('\n')
# print(user_metric_privilege)
# for k in user_metric_privilege.keys():
# 	print(k)
# 	for j in user_metric_privilege[k].keys():
# 		print(j)
# 		print(user_metric_privilege[k][j])
# 	print('\n')
# comb = combinations(range(1,7), 2) 
# for k in user_metric_privilege.keys():
# 	print(k)
# 	# print('1 2 3 4 5 6')
# 	for l in user_metric_privilege[k].keys():
# 		o = 1
# 		for m in user_metric_privilege[k].keys():
# 			# print((l,m))
# 			# print(str(o), end = ' ')
# 			# o += 1
# 			# if user_metric_privilege[k][l].difference(user_metric_privilege[k][m]) == user_metric_privilege[k][l]:
# 				# print('all', end = '<')			
# 			if user_metric_privilege[k][l].difference(user_metric_privilege[k][m]):
# 				print(user_metric_privilege[k][l].difference(user_metric_privilege[k][m]), end = '<')
# 			else:
# 				print('null', end = '<')
# 		print('\n')	
# 	print('\n')
