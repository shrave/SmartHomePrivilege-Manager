import pandas as pd

df = pd.read_excel('Device_Privilege_tags.xlsx')

# df = df.dropna()
# print(df.columns)
df['Device'] = list(zip(df['Device Name'], df['Acronym']))
df = df.drop(['Device Name', 'Acronym'], axis=1)
# print(df.columns)
func_dict = {}
type_dict = {}
for l,m,n,o in zip(df['Functionality'], df['Functionality Tags'], df['Device'], df['Device Type Tag']):
	a = o.split(',')
	b = m.split('-')
	if n not in func_dict.keys():
		func_dict[n] = {l:a}
		if l not in func_dict[n].keys():
			func_dict[n][l] = a
	else:
		func_dict[n][l] = a
	if n not in type_dict.keys():
		type_dict[n] = {l:b}
		if l not in type_dict[n].keys():
			type_dict[n][l] = b
	else:
		type_dict[n][l] = b
print(func_dict)
print('new')
print(type_dict)
# print(df.to_dict('series'))
# df.set_index("Device", drop=True, inplace=True)
# dictionary = df.to_dict(orient="index")
# print(dictionary)