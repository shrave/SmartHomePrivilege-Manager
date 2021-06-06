# SmartHomePrivilege-Manager
A privilege management system for smart home IoT devices. It takes fine-grained privileges from IoT devices and assigns only required privileges to the users.

It consists of devices, user groups and user classes. 
It requires privileges for each device as an input alongwith tags for each device.

It makes an arangement of privileges each user is capable of performing in all the home IoT devices.

It also tests whether the allocated privileges for the user and the task is least privilege or not based on the task.
It analyses security and privacy of devices based on privileges.

Implementation is based on this paper:

**Kanchi, Shravya, and Kamalakar Karlapalem. "A Multi Perspective Access Control in a Smart Home." Proceedings of the Eleventh ACM Conference on Data and Application Security and Privacy. 2021.**

Please cite this work, if using this code in your academic research. 

Example Scenario:

![A Kid User Krish requests for Cook Food task](https://github.com/shrave/SmartHomePrivilege-Manager/blob/master/Task-Krish.png)

To Setup the smart home, run the follwing files:

_execute_floorplan.py_ -> Imports the smart home devices, their instacnces, privileges and locations.
_main.py_ -> Imports the users of the smart home alongwith the restrictions set on them based on location, environment, device risk and time.
_setup_tasks.py_ -> Imports the tasks created by the administrator in accordance to the devices present in the house.

The execution of these files generates the following four pickled files, which are taken as an input in the task server(that grants permissions to users):
1. _safety.pkl_
2. _task_objects.pkl_
3. _user_list.pkl_
4. _devices_floorplan.pkl_
