#Class of a real user/person in the house.
class user(object):
	def __init__(self, Name):
		#List of user-groups.
		self.list_classes = []
		self.username = ''
		self.password = ''
		self.Name = Name
	#Computing the list of all capable privileges for all the device relationships.
	def capable_privileges(self):
		user_privileges = []
		for k in self.list_classes:
			user_privileges.append({k.device.label:k.privileges})
		self.user_privileges = user_privileges

	def register(self, username, password):
		self.username = username
		self.password = password

	def set_devices_user_groups(self, list_classes):
		self.list_classes = list_classes
	#list_classes -> the instances of user_groups instances.

#def request_task