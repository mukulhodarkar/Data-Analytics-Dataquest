#Replace "[serious]", "(Serious)", and "(serious)" with "[Serious]" for all of the titles in posts.
#You should only need to use one call to sub(), and one regex.

import csv
import re

file_contents = open("askreddit_2015.csv", "r", encoding="utf8")
posts_with_header = list(csv.reader(file_contents))
header_data = posts_with_header[0]
posts = posts_with_header[1:]

for record in posts:
    record[0] = re.sub("[\[\(][sS]erious[\)\]]", "[Serious]", record[0])
#If match found, re.sub() returns the result. Hence we have to store the result returned by the re.sub() function

    #print(record[0])


    #pass
