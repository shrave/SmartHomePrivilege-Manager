import pickle
from device import device

num_dict = {'1':3, '2':2, '3':1, '4':0}

def tag_number(n):
	if len(n)==4:
		n1 = n[0]
		n2 = n[2]
		return num_dict[n1]+num_dict[n2]
	else:
		np = n[0]
		return num_dict[np]


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
	if k:
		# print(device_instances[k.name])
		selected_devices[k.name] = {}
		# selected_devices.append(k)
		for i in k.user_groups.keys():
			if i!= 'Select background color':
				for l in k.user_groups[i]:
					if l not in selected_devices[k.name]:
						selected_devices[k.name][l] = [(i, device_instances[k.name][i])]
					else:
						selected_devices[k.name][l].append((i, device_instances[k.name][i]))		  

all_val = {}
for k in selected_devices.keys():
	print(k)
	# slot_dict = [1: 0, 2:0,3:0,4:0,5:0,6:0]
	slot_dict = {}
	tot_val = 0
	for j in selected_devices[k].keys():
		if j!= 7:
			print(j)
			count = 0
			su = 0
			for l in selected_devices[k][j]:
				# print(l[1])
				count += 1
				su += tag_number(str(l[1]))
			slot_dict[j] = (count, su)
			if j==1:
				tot_val =  su
	print(tot_val)
	print(slot_dict)
	print('\n')
	all_val[(k,tot_val)] = slot_dict

for k in all_val.keys():
	print(k[0])
	tot_val = k[1]
	slot_dict = all_val[k]
	for j in slot_dict.keys():
		print(j)
		print((slot_dict[j][1])/float(tot_val))
	print('\n')
# print(selected_devices)