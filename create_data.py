import pickle
from itertools import permutations 
import numpy as np

def get_random_groups(N):
	l = np.random.random_integers(1,6, size=N-1).tolist()
	l.append(1)
	return np.random.permutation(l)
#Retrieving previous device instances based on current floorplan.
with open('devices_floorplan.pkl', 'rb') as input:
    device_instances = pickle.load(input)

#36 device instances.
device_directory = {} #directory of devices for indexing purposes.
for i in device_instances:
	device_directory[i.label] = i

iterate_dict= { 2:400, 3:3500, 4:30000, 5:200000, 6:1650000 } 
#Number of users in the setup.
for N in range(2,7):
	#Creation of the random values for the dataset.
	for j in range(iterate_dict[N]):
		with open('Dataset/example'+ str(N)+ str(j) +'.sce', 'w') as f:
			f.write('#Format of user input for scenario setup.\n')
			f.write(str(N)+'\n')
			for k in range(N):
				f.write('User '+ str(k+1)+'\n')
			for k in device_directory.keys():
				f.write(k+'\n')
				for l in get_random_groups(N):
					f.write(str(l)+'\n')
		print('Finshed writing file '+str(N)+str(j))
	print('Finished ' + str(N))
