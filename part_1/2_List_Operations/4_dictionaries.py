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

weather_counts = {}
for item in weather:
    if item in weather_counts:
        weather_counts[item] += 1
    else:
        weather_counts[item] = 1
print("weather dictionary:")
print(weather_counts)
