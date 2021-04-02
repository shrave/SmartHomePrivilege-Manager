#The class which is an instance of a particular user group over a particular device.
class user_group(object):
	def __init__(self, code, automated, device_instance):
		self.code = int(code)
		#The binary encoding of primary, secondary, private, sensitive is type of user-group. 
		self.device = device_instance
		if automated != 1:
			if self.code == 1:
				self.group_name = 'Device Owner'
				self.type = '1111'
			if self.code == 2:
				self.group_name = 'Normal User'
				self.type = '0111'
			if self.code == 3:
				self.group_name = 'Limited User'
				self.type = '0011'
			if self.code == 4:
				self.group_name = 'Guest User'
				self.type = '0001'
			if self.code == 5:
				self.group_name = 'Child User'
				self.type = '0010'
			if self.code == 6:
				self.group_name = 'Guest Child'
				self.type = '0000'
		# else:
		# 	self.group_name = 'System User'
		# 	self.code = 7
		self.automated = int(automated)		

	#Function to get all the privileges of the device pertaining to the user-group.
	def privilege_selection(self):
		d = self.device.user_groups
		selected_privileges = []
		for k in d.keys():
			if self.code in d[k]:
				selected_privileges.append(k)
		self.privileges = selected_privileges
