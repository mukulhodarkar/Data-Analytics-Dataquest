def feature_counter(input_list, index, index_str, header_row = False):
    num_elements = 0
    if header_row == True:
        input_list = input_list[1:len(input_list)]
    for record in input_list:
        if record[index] == index_str:
            num_elements += 1
    return num_elements
def summary_statistics(input_list):
    num_japan_films = feature_counter(input_list, 6, "Japan", True)
    num_color_films = feature_counter(input_list, 2, "Color", True)
    num_films_in_english = feature_counter(input_list, 5, "English", True)
    films_disctionary = {"japan_films": num_japan_films, "color_films": num_color_films, "films_in_english": num_films_in_english}
    print (films_disctionary)
    return films_disctionary
file_variable = open("movie_metadata.csv", "r")
data = file_variable.read()
split_data = data.split('\n')
movie_data = []
for record in split_data:
    movie_details = record.split(',')
    movie_data.append(movie_details)
#print (movie_data)
summary = summary_statistics(movie_data)
