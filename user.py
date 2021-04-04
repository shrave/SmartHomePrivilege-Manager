from device import device
from devices import devices
#Class of a real user/person in the house.
class user(object):
	def __init__(self, Name):
		#List of user-groups.
		self.user_privilege_set = []
		self.username = ''
		self.password = ''
		self.Name = Name
	#Computing the list of all capable privileges for all the device relationships.
	def set_user_privilege_set(self):
		device_role_privileges = {}
		for device in self.device_list:
			device_role_privileges[device.label] = device.role_privileges
		self.user_privilege_set = device_role_privileges
		self.current_allowed_privileges = device_role_privileges

	def get_user_privilege_set(self):
		return self.user_privilege_set

	def register(self, username, password):
		self.username = username
		self.password = password

	def set_devices_user_groups(self, list_classes):
		self.groups = list_classes
	#groups -> the ordered list(according to first plan) of user-roles for all devices.

	def store_devices(self, device_list):
		self.device_list = device_list

	def get_devices(self):
		return self.device_list

	def apply_restrictions(self, restrictions):
		#restrictions = {'locations':[], 'environments':[], 'devices':[]}
		#Copying device_list.
		restricted_privileges = self.device_list
		#Removing not needed locations.
		for location in restrictions['locations']:
			for device in self.device_list:
			print(device.location)
			if device.location == location:
				del restricted_privileges[device.label]
		#Removing risky/restricted devices.
		for restrict_device in restrictions['devices']:
			for device in self.device_list:
				if device.label == restrict_device:
					del restricted_privileges[device.label]
		#Blocking restricted environments. Storing them, checking them at runtime if not in this datetime.
		for device in restricted_privileges:
			device.restricted_environment = restrictions['environments']
		self.updated_privileges = restricted_privileges
		return restricted_privileges



#Task Dictionary:
#{Task: [List of privileges]}
#def request_task