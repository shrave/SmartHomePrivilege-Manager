import pickle
from user_group import user_group
from user import user

#Dividing list into chunks of size n.
def divide_chunks(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

#Retrieving previous device instances based on current floorplan.
with open('devices_floorplan.pkl', 'rb') as input:
    device_instances = pickle.load(input)

#36 device instances.
device_directory = {} #directory of devices for indexing purposes.
for i in device_instances:
	device_directory[i.label] = i

#Code for input.
# user_list = []
# number_users = input("Enter the number of users")
# for j in range(len(number_users)):
# 	name = raw_input("Enter Name of User")
# 	user_list.append(user(name))

# for j in user_list:
# 	list_devices = [] #This is a temp list having devices for a particular user with groups.
# 	print("Device privileges for user " + str(j.Name))
# 	for k in device_instances:
# 		print("Enter the user group for the device in " + k.location+ " having label " + k.label )
# 		group = raw_input()
# 		list_devices.append(user_group(group, 0, k))
# 	j.set_devices_user_groups(list_devices)

#Taking input of user details from an input file with .sce extension.

with open('Dataset/example1.sce', 'r') as f:
	file_lines = f.readlines()

number_users = int(file_lines[1])
# Number of users in the input file.
file_lines = file_lines[2:]
user_list = file_lines[:number_users]
# User names in the input file.
file_lines = file_lines[number_users:]
usermapping = {} # A dictionary of users as key and list of device instances as values.
device_groups = list(divide_chunks(file_lines, number_users+1))
# Device groups are chunks of the device groups for each device.
for k in device_groups:
	device_name = str(k[0][:-1])
	i = 0
	for l in k[1:]:
		m = int(float(l))
		if i not in usermapping.keys():
			r = user_group(m,0, device_directory[device_name])
			r.privilege_selection()
			usermapping[i] = [r]
		else:
			r = user_group(m,0, device_directory[device_name])
			r.privilege_selection()
			usermapping[i].append(r)
		i += 1
users = []  # A list of user instances having all the device info and capabilities.

for k in usermapping.keys():
	u = user(str(user_list[k]))
	u.set_devices_user_groups(usermapping[k])
	u.capable_privileges() 
	users.append(u)

for k in users:
	print(k.Name)
	for l in k.user_privileges:
		for m in l.keys():
			print(m)
			print(l[m])

#Vary people in the setup and their relationships with the devices. 
#identify the threats in all cases.
#See how you can identify threats or indicators of threats. 