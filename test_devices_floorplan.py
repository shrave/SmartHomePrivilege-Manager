import pickle

with open('devices_floorplan.pkl', 'rb') as file:
	device_list = pickle.load(file)

for device in device_list:
	# print(dir(device))
	print(device.label)
	print(device.privileges)