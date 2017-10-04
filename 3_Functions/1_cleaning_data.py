f = open('movie_metadata.csv', 'r')
data = f.read()
data = data.split('\n')
movie_data = []
for line in data:
    record = line.split(',')
    movie_data.append(record)
print (movie_data)
