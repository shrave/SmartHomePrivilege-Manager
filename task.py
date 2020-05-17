#Task object class having attributes of the task for scheduling and checking devices.

#create task.
#least privilege, location, timing of device check.
class task(object):
	def __init__(self, name):
		self.name = name
		
	def create_task(self, location, time, requirement_tags):
		self.location = location
		self.time = time
		self.requirement_tags = requirement_tags
		return requirement_tags
		#check privilege tags and map it with requirement tags. 
		#load privilege tags from file.
	def validity_check(self, user):
		#Returns whether the user is capable of performing the task.

