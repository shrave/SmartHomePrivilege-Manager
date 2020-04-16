#The main body class of the user group. Made for convenience. 
#Instances of these are user-groups.
class user_group_body(object):
	def __init__(self, type, automated):
		self.type = int(type)
		#The binary encoding of primary, secondary, private, sensitive is type of user-group. 
		if automated != 1:
			if int(self.type) == 1111:
				self.name = 'Device Owner'
				self.code = 1
			if int(self.type) == 0111:
				self.name = 'Normal User'
				self.code = 2
			if int(self.type) == 0011:
				self.name = 'Limited User'
				self.code = 3
			if int(self.type) == 0001:
				self.name = 'Guest User'
				self.code = 4
			if int(self.type) == 0010:
				self.name = 'Child User'
				self.code = 5
			if int(self.type) == 0000:
				self.name = 'Guest Child'
				self.code = 6
		else:
			self.name = 'System User'
			self.code = 7
		self.automated = int(automated)
