f = open('crime_rates.csv', 'r')
data = f.read()
#print (data)
all_elements = data.split('\n')
five_elements = all_elements[0:5]
#print(type(five_elements))
#print(five_elements)
cities_list = []
for row in five_elements:
    split_elements = row.split(',')
#    city = split_elements[0]
#    cities_list.append(city)
    cities_list.append(split_elements[0])
print(cities_list)
