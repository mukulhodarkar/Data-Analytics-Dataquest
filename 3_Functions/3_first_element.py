def first_elts(input_lst):
    elts = []
    for each in input_lst:
        elts.append(each[0])
    return elts


f = open('movie_metadata.csv', 'r')
data = f.read()
data = data.split('\n')
movie = []
movie_data = []
for line in data:
    record = line.split(',')
    movie.append(record)
for line in movie:
    #record = movie_data[0]
    movie_data.append(record)
    #print (record)
#return (movie_data)
#print (movie_data)

movie_names = first_elts(movie_data)
print(movie_names[0:5])
