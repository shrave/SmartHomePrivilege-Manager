from device import device
from devices import devices
from user_group_body import user_group_body
from user_group import user_group
from user import user

import pandas as pd

df = pd.read_excel('Device List.xlsx')

functionalities = df['Functionality'].values.tolist() #A straight running list of functionalities.
devicenames = df['Device Name'].values.tolist() #A straight running list of device names.
acronyms = df['Acronym'].values.tolist() #A straight running list of acronyms.
user_tags = df['User Tags'] #A straight running list of user tags for each privileges.


list_of_list = []
l = []
# print(functionalities.split('nan	'))
for k in functionalities:
	if (str(k)=='nan') and (len(l)):
		list_of_list.append(l)
		l = []
	else:
		l.append(k)
tag_list = []
l = []
for k in user_tags:
	if (str(k)=='nan') and (len(l)):
		tag_list.append(l)
		l = []
	else:
		l.append(k)

keys = [] #List having tuples of device name followed by acronyms.
for j,k in zip(devicenames,acronyms):
	if 'nan'!= str(j):
		keys.append((j,k))

#All devices in the house- basic object function. It has each device name and acronym as key 
# and values as list of all privleges of the device.->privileges_dict
privileges_dict = {}
for j,k in zip(keys, list_of_list):
	if j[1] == 'MF':
		k.pop(0)
	privileges_dict[j] = k

#User based tags for each privilege in a device based dictionary of dictionaries. -> tags_device_list
tags_device_list = [] #check and match here functioanities and device and tags..
for j,k in zip(privileges_dict.keys(), tag_list):
	temp_privilege_user_tags = {}
	for m,n in zip(privileges_dict[j],k):
		temp_privilege_user_tags[m] = n
	tags_device_list.append({j: temp_privilege_user_tags})

#List of basic device objects for all 11 devices in the sceanrio. ->list_device_objects
list_device_objects = []
for k in privileges_dict.keys():
	list_device_objects.append(device(k[0],k[1],privileges_dict[k]))

#Storing privileges in the device objects and assigning groups.
for k in list_device_objects:
	for j in tags_device_list:
		for m in j.keys():
			if k.name == m[0]:
				k.store_privileges(j[m],'user')
				k.user_group_assignment()

for k in list_device_objects:
	print(k.name)
	for l in k.user_groups:
		print(l, k.user_groups[l])
	print('\n')


#List of all rooms/locations in the house - taken as input from the user ->locations.
locations = ['Outside', 'Living Room', 'Parents Room', 'Kids Room', 'Kitchen', 'Guest Room']

#Lists of instances/labels of devices in each of the rooms named by their list name below.
Living = ['L1', 'L2', 'P1', 'MF1', 'MF2', 'MF3', 'TV', 'Thermo1', 'Echo']
Outside = ['SSS', 'Lock']
Parents = ['L4', 'P3', 'MF4', 'MF5', 'Thermo2', 'S1']
Kids = ['L5', 'P4', 'MF8', 'MF9', 'Thermo4', 'S2']
Guest = ['L6', 'P5', 'MF10', 'MF11', 'Thermo5', 'S3']
Kitchen = ['L3', 'P2', 'MF6', 'MF7', 'Thermo3', 'Oven', 'Fridge']
#36 device instances are present in total.

#Mapping rooms wth their labels/instances of devices in a dictionary -> rooms_list
rooms_list = {'Living':Living, 'Outside':Outside, 'Parents':Parents, 'Kids': Kids, 'Guest': Guest, 'Kitchen':Kitchen}

#A list of all device instances in the house or instances of devices,
#having corresponding parent devices and locations marked.-> list_current_devices 
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



#Match groups with privileges. Generate the groups allowed for each privilege.
#See the set of privileges possible and identify the threats in all cases.
#Vary people in the setup and their relationships with the devices. 
#See how you can identify threats or indicators of threats. 