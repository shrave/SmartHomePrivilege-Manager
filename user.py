from user_group import user_group

#Class of a real user/person in the house.
class user(object):
	def __init__(self):
		#List of user-groups and their devices.
		self.list_classes = []
		self.username = ''
		self.password = ''

	#Computing the list of all capable privileges for all the device relationships.
	def capable_privilges(self):
		user_privileges = []
		for k in self.list_classes:
			user_privileges.append({k.label:k.privileges})
		self.user_privileges = user_privileges

	def register(self, username, password):
		self.username = username
		self.password = password

	def set_devices_user_groups(self, list_classes):
		self.list_classes = list_classes
#Decide whether this code is okay or not, also how animated must it be?

#def request_task