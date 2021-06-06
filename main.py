import pickle
from user_group import user_group
from user import user

#Dividing list into chunks of size n.
def divide_chunks(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

#Retrieving previous device instances based on current floorplan.
with open('devices_floorplan.pkl', 'rb') as file:
    device_instances = pickle.load(file)

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

with open('example1.sce', 'r') as f:
	file_lines = f.readlines()

number_users = int(file_lines[1])
# Number of users in the input file.
file_lines = file_lines[2:]
user_list = [] #List of user instances.
user_names = file_lines[:number_users]
for name in user_names:
	user_list.append(user(name.strip('\n')))
# User names in the input file.
file_lines = file_lines[number_users:]
usermapping = {} # A dictionary of users as key and list of device instances as values.
device_groups = list(divide_chunks(file_lines, number_users+1))
# print(len(device_groups))
# Device groups are chunks of the device groups for each device.
user_group_dictionary = {}
for name in user_names:
	user_group_dictionary[name.strip('\n')] = []
devices = [] #Devices in the config.
for k in device_groups:
	#Mapping devices in the data file to device config in previous step.
	device_name = str(k[0][:-1])
	# print(device_name)
	devices.append(device_directory[device_name])
	i = 0
	for l,u in zip(k[1:], user_names):
		m = int(float(l))
		# print(m)
		user_group_dictionary[u.strip('\n')].append(m)

#Giving the device instances to users and selecting the privileges group wise.
# print(user_group_dictionary)
# print(devices)
# print(user_list)

for j in user_list:
	list_devices = user_group_dictionary[j.Name] #This is a temp list having devices for a particular user with groups.
	user_device_set = []
	# print("Device privileges for user " + str(j.Name))
	for k,group in zip(devices,user_group_dictionary[j.Name]):
		# print("Enter the user group for the device in " + k.location+ " having label " + k.label )
		# group = int(input())
		# list_devices.append(int(group))
		# print(group)
		k.privileges_by_user_group(int(group))
		# print(k.role_privileges)
		user_device_set.append(k)
	j.set_devices_user_groups(user_group_dictionary[j.Name])
	j.store_devices(user_device_set)
	j.set_user_privilege_set()

new_users = []
for u in user_list:
	print(u.Name)
	# print(u.get_user_privilege_set())
	new_users.append(u)

user_list = new_users
#Creation of restrictions for each user. Here every attribute is not allowed.
#Selected users and their restrictions.
restrictions_by_users = {'User 1':{'locations':['Outside'], 'environments':['summer', 'morning'], 'devices':[]},'User 4':{'locations':['Outside'], 'environments':['summer', 'evening'], 'devices':[]}}
  
new_users = []
#Apply restrictions.
print(len(user_list))
for u in user_list:
	if u.Name in restrictions_by_users.keys():
		u.apply_restrictions(restrictions_by_users[u.Name])
		print(u.Name)
		print(u.updated_privileges)
		#Updated privileges has final privileges that the user can use.
		#Updated privileges has all devices removed except environments.
		for device in u.updated_privileges:
			print(device.label)
			print(device.role_privileges)
		# print("***********")
		new_users.append(u)
	else:
		temp_dict = {'locations':[], 'environments':[], 'devices':[]}
		u.apply_restrictions(temp_dict)
		new_users.append(u)

user_list = new_users
save_object(user_list, 'user_list.pkl')
#Create tasks.
#Assign privileges to each task.
#Check exclusivity of tasks.
#Removal of insider threats.
#identify the threats in all cases.
#See how you can identify threats or indicators of threats. 
#System user marks a pattern of malicious actor-> parameters noted.
#System can check if there is a match between system user and current user-> check anamoly.
