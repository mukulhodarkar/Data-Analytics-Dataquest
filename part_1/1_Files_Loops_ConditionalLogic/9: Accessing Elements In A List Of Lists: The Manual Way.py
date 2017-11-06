f = open('crime_rates.csv', 'r')
data = f.read()
#print (data)
all_elements = data.split('\n')
#print(all_elements)
five_elements = all_elements[0:5]
#print(type(five_elements))
#print(five_elements)
cities_list = []
final_data = []
final_data_string_format = []
for row in five_elements:
    split_row = row.split(',')
    #print(split_elements)
    final_data.append(split_row)
    final_data_string_format.append(split_row[0])

print(final_data)
print(final_data_string_format)

for row in final_data:
    #city = row[0]
    cities_list.append(row[0])
print(cities_list)
