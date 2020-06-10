import pickle
from device import device

with open('../safety.pkl', 'rb') as input:
    device_instances = pickle.load(input)

#Device Name, privelege and security tag.
# for k in device_instances.keys():
# 	print(k)
# 	for j in device_instances[k]:
# 		print(j)
# 		print(device_instances[k][j])

with open('../devices.pkl', 'rb') as input:
    devices = pickle.load(input)

selected_devices = {}
for k in devices:
	# if (k.name == 'Smart Lock') or (k.name == 'Smart Oven') or (k.name == 'Smart shower'):
	if k.name == 'Smart Oven':
		# print(device_instances[k.name])
		selected_devices[k.name] = {}
		# selected_devices.append(k)
		for i in k.user_groups.keys():
			# print(i)
			for l in k.user_groups[i]:
				if l not in selected_devices[k.name]:
					selected_devices[k.name][l] = [(i, device_instances[k.name][i])]
				else:
					selected_devices[k.name][l].append((i, device_instances[k.name][i]))		  
		# print('\n')
for k in selected_devices.keys():
	print(k)
	for j in selected_devices[k].keys():
		if j!= 7:
			print(j)
			for l in selected_devices[k][j]:
				print(l)
	print('\n')
# print(selected_devices)