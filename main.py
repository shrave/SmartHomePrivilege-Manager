from device import device
from devices import devices
from user_group_body import user_group_body
from user_group import user_group
from user import user

import pandas as pd

df = pd.read_excel('Device List.xlsx')

functionalities = df['Functionality'].values.tolist()
devicenames = df['Device Name'].values.tolist() 
acronyms = df['Acronym'].values.tolist()

list_of_list = []
l = []
for k in functionalities:
	if str(k)=='nan':
		list_of_list.append(l)
		l = []
	else:
		l.append(k)
keys = []
for j,k in zip(devicenames,acronyms):
	if 'nan'!= str(j):
		keys.append((j,k))

privileges_dict = {}
for j,k in zip(keys, list_of_list):
	privileges_dict[j] = k
#All devices in the house- basic object function.
list_device_objects = []
for k in privileges_dict.keys():
	list_device_objects.append(device(k[0],k[1],privileges_dict[k]))
for j in list_device_objects:
	print(j.name)
print(len(list_device_objects))
locations = ['Outside', 'Living Room', 'Parents Room', 'Kids Room', 'Kitchen', 'Guest Room']

location_device = {}

Living = ['L1', 'L2', 'P1', 'MF1', 'MF2', 'MF3', 'TV', 'Thermo1', 'Echo']
Outside = ['SSS', 'Lock']
Parents = ['L4', 'P3', 'MF4', 'MF5', 'Thermo2', 'S1']
Kids = ['L5', 'P4', 'MF8', 'MF9', 'Thermo4', 'S2']
Guest = ['L6', 'P5', 'MF10', 'MF11', 'Thermo5', 'S3']
Kitchen = ['L3', 'P2', 'MF6', 'MF7', 'Thermo3', 'Oven', 'Fridge']
#36 device instances
rooms_list = {'Living':Living, 'Outside':Outside, 'Parents':Parents, 'Kids': Kids, 'Guest': Guest, 'Kitchen':Kitchen}
list_current_devices = []

for m in list_device_objects:
	for k in rooms_list.keys():
		for l in rooms_list[k]:
			if m.acronym == l: 
				list_current_devices.append(devices(m, k , l ))
			else:
				if ('L' in l) and (m.acronym == 'L') and (l != 'Lock'):
					list_current_devices.append(devices(m, k , l ))	
				if ('P' in l) and (m.acronym == 'P'):
					list_current_devices.append(devices(m, k , l ))	
				if ('MF' in l) and (m.acronym == 'MF'):
					list_current_devices.append(devices(m, k , l ))	
				if ('S' in l) and (m.acronym == 'S') and (l != 'SSS'):
					list_current_devices.append(devices(m, k , l ))	
				if ('Thermo' in l) and (m.acronym == 'Thermo'):
					list_current_devices.append(devices(m, k , l ))	

#Set the devices solid and their instances.
#Vary people in the setup and their relationships with the devices. 
#See the set of privileges possible and identify the threats in all cases.
#See how you can identify threats or indicators of threats. 