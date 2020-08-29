f = open('only_mat')
# for k in f.readlines():
p = f.readlines()

list_of_mat = {}
mat = []
for k in range(len(p)):
	if p[k][0].isalpha():
		mat.append((p[k+1].strip()).split())
		mat.append((p[k+3].strip()).split())
		mat.append((p[k+5].strip()).split())
		list_of_mat[p[k].strip()] = mat
		mat = []

mat = []
int_list = {}
lmat  = []
for k in list_of_mat.keys():
	for n in list_of_mat[k]:
		for l in n:	
			# print(l)
			o = int(l)
			mat.append(o)
			# print(type(o))
		lmat.append(mat)
		mat = []
	int_list[k] = lmat
	lmat = []
# print(int_list)

for k in int_list.keys():
	print(k)
	a = int_list[k][0][0]+int_list[k][1][0]+int_list[k][0][1]
	b = int_list[k][2][2]+int_list[k][1][2]+int_list[k][2][1]
	print(a,b)
	if(a>b):
		print('high risk')
	elif(a<b):
		print('low risk')
	else:
		print('moderate risk')