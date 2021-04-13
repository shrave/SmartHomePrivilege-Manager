from device import device
from devices import devices
from user import user
import pandas as pd
import pickle

#Function for pickling variables.
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

df = pd.read_excel('Device List.xlsx')

functionalities = df['Functionality'].values.tolist() #A straight running list of functionalities.
devicenames = df['Device Name'].values.tolist() #A straight running list of device names.
acronyms = df['Acronym'].values.tolist() #A straight running list of acronyms.
user_tags = df['User Tags'] #A straight running list of user tags for each privileges.

#A list consisting of order-wise device functionalities grouped as lists ->list_of_list
list_of_list = []
l = []
for k in functionalities:
	if (str(k)=='nan') and (len(l)):
		list_of_list.append(l)
		l = []
	else:
		l.append(k)
list_of_list.append(l)

#A list consisting of orderwise user tags for a device in the form of lists. ->tag_list. 
# tag_list = []
# l = []
# for k in user_tags:
# 	if (str(k)=='nan') and (len(l)):
# 		tag_list.append(l)
# 		l = []
# 	else:
# 		l.append(k)
# tag_list.append(l)
#(Unused)

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
# print(privileges_dict[('Amazon Echo', 'Echo')])
#Combining columns functionality and user tags.
lists = []
l =[]
for index, row in df.iterrows(): 
	if (str(row['Functionality']) =='nan') and (len(l)):
		lists.append(dict(l))
		l = []
	else:
		l.append((row["Functionality"], row["User Tags"]))
lists.append(dict(l))

#User based tags for each privilege in a device based dictionary of dictionaries. -> tags_device_list
tags_device_list = []
for j,k in zip(keys, lists):
	tags_device_list.append({j:k})

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
				k.device_risk()
# print(list_device_objects)
# for device in list_device_objects:
# 	print(device.name)
# 	print(device.user_groups)
# 	print(device.risk)
# 	print('///////////////////')
#Proper assignment of user groups done to each privilege here based on tags.

#Environments are spacio-temporal constructs.
from datetime import date, datetime, time

Y = 2000 # dummy leap year to allow input X-02-29 (leap day)
environment_ranges= {'winter': (date(Y,  1,  1),  date(Y,  3, 20)),
           'spring':(date(Y,  3, 21),  date(Y,  6, 20)),
           'summer': (date(Y,  6, 21),  date(Y,  9, 22)),
           'autumn': (date(Y,  9, 23),  date(Y, 12, 20)),
           'winter': (date(Y, 12, 21),  date(Y, 12, 31)),
           'morning':(time(5,0,0), time(11,59,59)), 
           'afternoon':(time(12,0,0), time(16,59,59)),
           'evening':(time(17,0,0), time(20,59,59)), 
           'night (PM)':(time(21,0,0), time(23,59,59)), 
           'night (AM)':(time(0,0,0), time(4,59,59))
           }

times_to_check = [
'2015-02-03 13:48:41',
'2015-02-06 19:42:33',
'2015-02-07 08:22:11', 
'2015-02-11 02:23:11',
'2015-02-14 22:45:41'
]

# for check in times_to_check:
#     check_time = datetime.strptime(check, "%Y-%m-%d %H:%M:%S").time()
#     for k, v in environment_ranges.iteritems():
#         if v[0] <= check_time <= v[1]:
#             print check, k

# def get_environments(now):
#     if isinstance(now, datetime):
#         now = now.date()
#     now = now.replace(year=Y)
#     return next(season for season, (start, end) in environment_ranges
#                 if start <= now <= end)

# print(get_environments(date.today()))

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

device_label_master_list = {}
#Pickling the current devices based on floorplan to use in the future.
for device in list_current_devices:
	print(device.name)
	print(device.label)
	if device.name not in device_label_master_list.keys():
		device_label_master_list[device.name]= [device.label]
	else:
		device_label_master_list[device.name].append((device.label))
	print(device.location)
	print(device.privileges)
	print(device.user_groups)
	print(device.risk)
	print('**************')
print(device_label_master_list)
save_object(list_current_devices, 'devices_floorplan.pkl')
save_object(list_device_objects, 'devices.pkl')
save_object(device_label_master_list,'device_label.pkl')