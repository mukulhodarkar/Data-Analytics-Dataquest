def is_usa(input_list):
    if input_list[6] == 'USA':
        return True
    else:
        return False

file_variable = open('movie_metadata.csv', 'r')
data = file_variable.read()
split_data = data.split('\n')

movie_data = []
for line in split_data:
    record = line.split(',')
    movie_data.append(record)
#print(movie_data[1][2]) #list of lists is creaeted now i can access any element by using indices.

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

wonder_woman_usa = is_usa(wonder_woman)
print (wonder_woman_usa)
