import numpy as np

f = open('../security_privacy_compare', 'r')
k = f.read()
# for i in k:
# 	print(i)
# print(k[8])
# device_read = []
# curr_read = []
# for i in k:
# 	if i!= '\n':
# 		# print(type(i[0]))
# 		if (i[0]== '{') or (i[0]== 's'):
# 			curr_read.append(i)
# 		else:
# 			device_read.append(curr_read)
# 			print(curr_read)
# 			curr_read = []
# 			curr_read.append(i)
# 	# print(curr_read)
# device_read.append(curr_read)
# device_read.remove([])
# print(len(device_read))
# for k in device_read:
# 	for i in k:
# 		print(i.split('<'))

# print(k.split('\n\n\n'))
for i in k.split('\n\n\n'):
	# print(i)
	for j in (i.split('\n')):
		print(j)
		for l in j.split('<'):
			if l=='set()':
				print(0, end =" ")
			elif (l=='\n') or (len(l)<2):
				pass
			else:
				y = l.split(',')
				print(len(y), end = ' ')
		print('\n') 
