mixed_list=[256,'kigali',250,254,'nairobi']
city_code=[]
cities=[]
for item in mixed_list:
		if type(item)==int:
			city_code.append(item)
		elif type(item)==str:
			cities.append(item)
		else:
			pass
print city_code
print cities