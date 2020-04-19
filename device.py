#Master device class for a device. Not the instances of different devices.
class device(object):
	def __init__(self, name, acronym, privileges):
		self.name = name
		self.acronym = acronym
		self.user_privilege = {}
		self.privilege_type = {}
		self.user_groups = {}
		self.privileges = privileges
#privileges is a list of privileges.
#user_privileges are a dictionary of privileges and tags associated to list.
	# "Un/lock smart lock":'private','sensitive', 'secondary','primary' - d dictionary
		def store_privileges(self, d, k):
			self.user_privilege = d
			self.privilege_type = k
	# "Un/lock smart lock": "entry-exit" -> k dictionary
		def user_group_assignment(self):
	#Assigning a privilege group to corresponding user members.
			d = self.user_privilege
			#d is a copied variable.
			user_groups = {}
			#user_groups is a temporary dictionary to be copied to self.user_groups
			groups = []
			for k in d.keys():
				if 'primary' in d[k]:
					groups = [1,7]
				elif 'secondary' in d[k]:
					groups = [1,2,7]
				elif 'private' in d[k]:
					if 'sensitive' in d[k]:
						groups = [1,2,3,7]
					else:
						groups = [1,2,3,5,7] 
				elif 'sensitive' in d[k]:
					groups = [1,2,3,4,7]
				else:
					groups = [1,2,3,4,5,6,7]
				user_groups[k] = groups
				groups = []
			self.user_groups = user_groups				
				
				

