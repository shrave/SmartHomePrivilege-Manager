from device import device

class devices(device):
	def __init__(self, *args):
		if type(args[0]) is device:
			self.__dict__ = args[0].__dict__.copy()
			location = args[1]
			label = args[2]
			self.location = location
			self.label = label
			#A dictionary consisting of user instances with these time slots.->time_slots
		else:
			super(device, self).__init__(*args[:4])
			location = args[3]
			label = args[4]
			self.location = location
			self.label = label
		# self.restricted_environment = 'None'
