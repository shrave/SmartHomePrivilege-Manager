from device import device
from devices import devices
from user_group_body import user_group_body

#The class which is an instance of a particular user group over a particular device.

class user_group(devices, user_group_body):
	def __init__(self):
		super(device, self).__init__()
		super(user_group_body, self).__init__()

	#Function to get all the privileges of the device pertaining to the user-group.
	def privilege_selection(self):
		d = self.user_groups
		#Copied the variable.
		selected_privileges = []
		for k in d.keys():
			if self.code in d[k]:
				selected_privileges.append(k)
		m = self.privilege_type
		self.privilege_type = dict((k, m[k]) for k in selected_privileges 
                                        if k in m)
		self.privileges = selected_privileges
