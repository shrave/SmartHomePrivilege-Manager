#The class which is an instance of a particular user group over a particular device.
class user_group(object):
	def __init__(self, type, automated, device_instance):
		self.type = int(type)
		#The binary encoding of primary, secondary, private, sensitive is type of user-group. 
		self.device = device_instance
		if automated != 1:
			if self.type == '1111':
				self.group_name = 'Device Owner'
				self.code = 1
			if self.type == '0111':
				self.group_name = 'Normal User'
				self.code = 2
			if self.type == '0011':
				self.group_name = 'Limited User'
				self.code = 3
			if self.type == '0001':
				self.group_name = 'Guest User'
				self.code = 4
			if self.type == '0010':
				self.group_name = 'Child User'
				self.code = 5
			if self.type == '0000':
				self.group_name = 'Guest Child'
				self.code = 6
		else:
			self.group_name = 'System User'
			self.code = 7
		self.automated = int(automated)		

	#Function to get all the privileges of the device pertaining to the user-group.
	def privilege_selection(self):
		d = self.device.user_groups
		selected_privileges = []
		for k in d.keys():
			if self.code in d[k]:
				selected_privileges.append(k)
		m = self.privilege_type
		self.privilege_type = dict((k, m[k]) for k in selected_privileges 
                                        if k in m)
		self.privileges = selected_privileges
