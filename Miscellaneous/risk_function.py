import pickle

#Load security of devices.
with open('../safety.pkl', 'rb') as input:
	safety_dict = pickle.load(input)

# for device in safety_dict:
# 	print(device)
# 	print(safety_dict[device])
# 	print("****************")

tag_dict = {}
for k in safety_dict.keys():
	print(k)
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
	# print(S1_list)
	# print(S2_list)
	# print(S3_list)
	# print(P1_list)
	# print(P2_list)
	# print(P3_list)
	# print('***************')
# for device in tag_dict:
# 	print(device)
# 	print(tag_dict[device])
for k in tag_dict.keys():
	print(k)
	# print('\n')
	risk_matrix = []
	# print(len(tag_dict[k][0]))
	# print(len(tag_dict[k][1]))
	for j in range(len(tag_dict[k][0])):
		sec_levels = []
		for l in range(len(tag_dict[k][1])):
			# print(j, end = ' ')
			# print(l, end = ' ')
			# print(tag_dict[k][0][j].union(tag_dict[k][1][l]), end = '<')
			sec_levels.append(len(tag_dict[k][0][j].union(tag_dict[k][1][l])))
		# print('\n')
		risk_matrix.append(sec_levels)
	# print('\n')

	a = risk_matrix[0][0]+risk_matrix[1][0]+risk_matrix[0][1]
	b = risk_matrix[2][2]+risk_matrix[1][2]+risk_matrix[2][1]
	# print(a,b)
	if(a>b):
		print('high risk')
	elif(a<b):
		print('low risk')
	else:
		print('moderate risk')
	print('\n')