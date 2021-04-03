import pickle
from user import user

#Retrieving previous device instances based on current floorplan.
with open('devices_floorplan.pkl', 'rb') as input:
    device_instances = pickle.load(input)

#36 device instances.
device_directory = {} #directory of devices for indexing purposes.
for i in device_instances:
	device_directory[i.label] = i

#Code for input.
user_list = []
print("Enter the number of users")
number_users = input()
for j in range(len(number_users)):
	name = raw_input("Enter Name of User")
	user_list.append(user(name))

for j in user_list:
	list_devices = [] #This is a temp list having devices for a particular user with groups.
	user_device_set = []
	print("Device privileges for user " + str(j.Name))
	for k in device_instances:
		print("Enter the user group for the device in " + k.location+ " having label " + k.label )
		group = raw_input()
		list_devices.append(int(group))
		k.privileges_by_user_group(group)
		user_device_set.append(k)
	j.set_devices_user_groups(list_devices)
	j.store_devices(user_device_set)

for u in user_list:
	print(u.Name)
	print(u.get_devices_user_groups())


#Create tasks.
#Assign privileges to each task.
#Check exclusivity of tasks.
#Removal of insider threats.
#identify the threats in all cases.
#See how you can identify threats or indicators of threats. 
#System user marks a pattern of malicious actor-> parameters noted.
#System can check if there is a match between system user and current user-> check anamoly.
