import pandas as pd
f = open('user','r')
list_groups = []
device_list = []
for k in f.readlines():
	if len(k.split()):
		list_groups.append(k.split())
	else:
		device_list.append(list_groups)
		list_groups = []
device_list[0].pop(0)
print(device_list)
print(len(device_list))
device_taglist = []
tag_list = []
for j in device_list:
	for k in j:
		if k==['1']:
			tag_list.append(['primary'])
		elif k==['1,2']:
			tag_list.append(['secondary'])
		elif k==['1,2,3']:
			tag_list.append(['private','sensitive'])
		elif k==['1,2,3,5']:
			tag_list.append(['private'])
		elif k==['1,2,3,4']:
			tag_list.append(['sensitive'])
		elif k==['1,2,3,4,5,6']:
			tag_list.append([' '])
		else:
			tag_list.append(['private','non-sensitive'])
	device_taglist.append(tag_list)
	tag_list = []
print(device_taglist)
f = open('user_taglist', 'w+')
for k in device_taglist:
	for l in k:
		f.write(" ".join(l))
		f.write('\n')
	f.write('\n')
f.close()