import pickle
from user_group import user_group
from user import user




#Retrieving previous device instances based on current floorplan.
with open('devices_floorplan.pkl', 'rb') as input:
    device_instances = pickle.load(input)



#See the set of privileges possible for a new set of users.
#Vary people in the setup and their relationships with the devices. 
#identify the threats in all cases.
#See how you can identify threats or indicators of threats. 