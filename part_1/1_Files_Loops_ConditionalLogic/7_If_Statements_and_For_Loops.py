#Create a new list, five_hundred_list, that contains only the elements from crime_rates that are greater than 500

#Answer:
#1. Make a list of lists and select only crime_rates from it. i.e. the [1] index valuesself.
    #1. open file
    #3. Split on '\n'
    #4. Each row, split by ','
    #5.
#2. Create a new list five_hundred_listself.
    #1. Select only values at [1] index i.e. crime_rates
    #2. Check if crime_rate > 500
    #3. Append it to the list


f = open("crime_rates.csv", "r")
data = f.read()
rows = data.split('\n')
split_list = []
crime_rates = []
for row in rows:
    split_list.append(row.split(','))
for row in split_list:
    #crime_rate = row[1]
    crime_rates.append(row[1])

five_hundred_list = []
for record in crime_rates:
    if record > '500':
        five_hundred_list.append(record)
print(five_hundred_list)
