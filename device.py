import pickle
#Master device class for a device. Not the instances of different devices.
class device(object):
	def __init__(self, name, acronym, privileges):
		self.name = name
		self.acronym = acronym
		self.user_privilege = {}
		self.privilege_type = {}
		self.user_groups = {}
		self.privileges = privileges
		self.risk = 'default'
#privileges is a list of privileges.
#user_privileges are a dictionary of privileges and tags associated to list.
	# "Un/lock smart lock":'private','sensitive', 'secondary','primary' - d dictionary
	def store_privileges(self, d, tag):
		if tag =='user':
			self.user_privilege = d
		if tag == 'function':
			self.privilege_type = d
	# "Un/lock smart lock": "entry-exit" -> k dictionary
	def user_group_assignment(self):
	#Assigning a privilege group to corresponding user members.
		d = self.user_privilege
			#d is a copied variable.
		user_groups = {}
			#user_groups is a temporary dictionary to be copied to self.user_groups
			#having privileges and their corresponding groups allowed to perform it.
		groups = []
		for k in d.keys():
			if 'primary' in d[k]:
				groups = [1]
			elif 'secondary' in d[k]:
				groups = [1,2]
			elif 'private' in d[k]:
				if 'sensitive' in d[k]:
					groups = [1,2,3]
				elif 'non-sensitive' in d[k]:
					groups = [1,2,3,4,5]
				else:
					groups = [1,2,3,5] 
			elif 'sensitive' in d[k]:
				groups = [1,2,3,4]
			else:
				groups = [1,2,3,4,5,6]
			user_groups[k] = groups
			groups = []
		self.user_groups = user_groups

	def device_risk(self):

	#Load security of devices.
		with open('safety.pkl', 'rb') as input:
			safety_dict = pickle.load(input)
		k = self.name
		tag_dict = []
		S1_list = []
		S2_list = []
		S3_list = []
		P1_list = []
		P2_list = []
		P3_list = []
		# print(safety_dict[k])
		for j in safety_dict[k].keys():
			# print(j)
			K = safety_dict[k][j]
			# print(K)
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

		tag_dict.append([set(S1_list),set(S2_list),set(S3_list)])
		tag_dict.append([set(P1_list),set(P2_list),set(P3_list)])
		# print(tag_dict)
		risk_matrix = []

		for j in range(len(tag_dict[0])):
			sec_levels = []
			for l in range(len(tag_dict[1])):

				sec_levels.append(len(tag_dict[0][j].union(tag_dict[1][l])))
			risk_matrix.append(sec_levels)
		# print(risk_matrix)
		a = risk_matrix[0][0]+risk_matrix[1][0]+risk_matrix[0][1]
		b = risk_matrix[2][2]+risk_matrix[1][2]+risk_matrix[2][1]

		if(a>b):
			print('high risk')
			self.risk = 'High risk'
		elif(a<b):
			print('low risk')
			self.risk = 'Low risk'
		else:
			print('moderate risk')
			self.risk = 'Moderate risk'

	def privileges_by_user_group(self,group_code):
		d = self.user_groups
		selected_privileges = []
		for k in d.keys():
			if group_code in d[k]:
				selected_privileges.append(k)
		self.role_privileges = selected_privileges
		# return selected_privileges
				
	def get_privileges_by_user_group(self,group_code):
		d = self.user_groups
		selected_privileges = []
		for k in d.keys():
			if group_code in d[k]:
				selected_privileges.append(k)
		return selected_privileges

