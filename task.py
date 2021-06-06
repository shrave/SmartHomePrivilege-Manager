#Task object class having attributes of the task for scheduling and checking devices.

#create task.
#least privilege, location, timing of device check.
class task(object):
	def __init__(self, name, privileges_allowed, time):
		self.name = name
		self.privileges_allowed = privileges_allowed
		self.time = time
		#users, devices and privileges in it.
		#Generating random numbers for testing. But need to properly specify.
	def add_details(self, location, time):
		self.location = location
		#self.requirement_tags = requirement_tags
		#return requirement_tags
		#check privilege tags and map it with requirement tags. 
		#load privilege tags from file.
	def validity_check(self, user):
		#Returns whether the user is capable of performing the task.
		filtered_privileges = {}
		u = user
		for device in u.updated_privileges:
			# print(device.label)
			# print(device.role_privileges)
			for task_device in self.privileges_allowed:
				# print(task_device.label)
				# print(device.label)
				if device.label == task_device.label:
					# print('matched')
					for privilege in self.privileges_allowed[task_device]:
						# print(privilege)
						if privilege in device.role_privileges:
							if task_device not in filtered_privileges:
								filtered_privileges[task_device.label] = [privilege]
							else:
								filtered_privileges[task_device.label].append(privilege)
		# print(filtered_privileges)
		return filtered_privileges


		
