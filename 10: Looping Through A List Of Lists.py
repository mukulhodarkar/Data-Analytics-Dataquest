file = open('crime_rates.csv', 'r')
data = file.read()
#print(data)
rows = data.split('\n')
#print(rows)
final_data = []
#print("final data:", final_data)#Create an empty list. And also when program execute 2nd time, we need a clean list.
for row in rows:
    split_row = row.split(',')
    #print(split_row)
    final_data.append(split_row)

five_elements=final_data[0:5]
print("five_elements:", five_elements)
crime_rates = []
for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)
print(crime_rates)
