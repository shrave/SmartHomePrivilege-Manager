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
print(df)
# df = df.dropna()
safety_dict = {}
for j,k,l in zip(df['Device Name'], df['Functionality'], df['Critical Tags']):
	if j not in safety_dict.keys():
		safety_dict[j] = {}
	if k not in safety_dict[j].keys():
		safety_dict[j][k] = l
print(safety_dict)
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

tag_dict = {}
for k in safety_dict.keys():
	# print(k)
	tag_dict[k] = []
	S1_list = []
	S2_list = []
	S3_list = []
	P1_list = []
	P2_list = []
	P3_list = []
	for j in safety_dict[k].keys():
		# print(j)
		K = safety_dict[k][j]
		if '1S' in str(K):
			S1_list.append(j)
		if '1P' in str(K):
			P1_list.append(j)
		if '2S' in str(K):
			S2_list.append(j)
		if '3S' in str(K):
			S3_list.append(j)
		if '2P' in str(K):
			P2_list.append(j)
		if '3P' in str(K):
			P3_list.append(j)
		# print(user_metric_privilege[k][j])
	# print('\n')
	tag_dict[k].append([set(S1_list),set(S2_list),set(S3_list)])
	tag_dict[k].append([set(P1_list),set(P2_list),set(P3_list)])
	print(S1_list)
	print(S2_list)
	print(S3_list)
	print(P1_list)
	print(P2_list)
	print(P3_list)
print(tag_dict)
comb = combinations(range(1,7), 2) 
for k in user_metric_privilege.keys():
	print(k)
	# print('1 2 3 4 5 6')
	for l in user_metric_privilege[k].keys():
		o = 1
		for m in user_metric_privilege[k].keys():
			# print((l,m))
			# print(str(o), end = ' ')
			# o += 1
			# if user_metric_privilege[k][l].difference(user_metric_privilege[k][m]) == user_metric_privilege[k][l]:
				# print('all', end = '<')			
			if user_metric_privilege[k][l].difference(user_metric_privilege[k][m]):
				print(user_metric_privilege[k][l].difference(user_metric_privilege[k][m]), end = '<')
			else:
				print('null', end = '<')
		print('\n')	
	print('\n')
for k in tag_dict.keys():
	print(k)
	# print(len(tag_dict[k][0]))
	# print(len(tag_dict[k][1]))
	for j in range(len(tag_dict[k][0])):
		for l in range(len(tag_dict[k][1])):
			# print(j, end = ' ')
			# print(l, end = ' ')
			# print(tag_dict[k][0][j].union(tag_dict[k][1][l]), end = '<')
			print(len(tag_dict[k][0][j].union(tag_dict[k][1][l])), end = ' ')			
		print('\n')
	print('\n')