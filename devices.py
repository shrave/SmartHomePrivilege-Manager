from device import device

class devices(device):
	# @classmethod
	# def from_parent(cls, parent):
	# 	return cls(parent.name,parent.acronym,parent.privileges)

	def __init__(self, *args):
		if type(args[0]) is device:
			self.__dict__ = args[0].__dict__.copy()
			location = args[1]
			label = args[2]
			self.location = location
			self.label = label
		else:
			super(device, self).__init__(*args[:4])
			location = args[3]
			label = args[4]
			self.location = location
			self.label = label
