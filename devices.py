from .device import device

class devices(device):
	def __init__(self, location, label):
		self.location = location
		self.label = label
		super(device, self).__init__()

