f = open('la_weather.csv', 'r')
data = f.read()
data = data.split('\n')
weather_data = []
for line in data:
    record = line.split(',')
    weather_data.append(record)
#print(weather_data)

weather = []
for record in weather_data:
    weather.append(record[1])
print(weather)
