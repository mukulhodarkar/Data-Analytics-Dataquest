#Create a list of integers named int_crime_rates that contains just the crime rates - as integers - from the list rows.

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])

int_crime_rates = []

for row in rows:
    split_data = row.split(',')

    int_crime_rates.append(int(split_data[1]))

#print(type(split_data))
#print(type(crime_rate))
print(int_crime_rates)
