f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
