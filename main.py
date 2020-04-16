from .device import device
from .devices import devices
from .user_group_body import user_group_body
from .user_group import user_group
from .user import user

import openpyxl

wb_obj = openpyxl.load_workbook('Device List.xlsx')
sheet_obj = wb_obj.active 

#Set the devices solid and their instances.
#Vary people in the setup and their relationships with the devices. 
#See the set of privileges possible and identify the threats in all cases.
#See how you can identify threats or indicators of threats. 