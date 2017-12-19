file = open('crime_rates.csv', 'r')
data = file.read()
#print(data)
rows = data.split('\n')
#print(rows)
final_data = []
#print("final data:", final_data)#Create an empty list. And also when program execute 2nd time, we need a clean list.
for row in rows:
    split_row = row.split(',') #mistakes I was doing: 1. Splitting data, rowS...instead we need to split the individual row and not the whole file.
    #print(split_row)
    final_data.append(split_row)
#print(final_data)
