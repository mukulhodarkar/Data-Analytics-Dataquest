#Use square bracket notation to make the code account for both capitalizations of "Reddit",
#count how many posts contain 'of Reddit' or 'of reddit' in the title.
#Assign the resulting count to of_reddit_count.
#Escape the square bracket characters to count the number of posts in our data set that contain the "[Serious]" tag.
#Assign the count to serious_count.

import csv
import re

file_contents = open("askreddit_2015.csv", "r", encoding="utf8")
posts_with_header = list(csv.reader(file_contents))
header_data = posts_with_header[0]
posts = posts_with_header[1:]

of_reddit_count = 0
serious_count = 0
serious_count_final = 0
serious_start_count = 0
serious_end_count = 0

for record in posts:
    if re.search("of [rR]eddit", record[0]) is not None:
        of_reddit_count += 1
#1. while counting [Serious] also include [serious]
#2. Refine the code so that it counts how many posts have the serious tag enclosed in either square brackets or parentheses.
#3. Use the "^" character to count how many posts include the serious tag at the beginning of the title.
#Assign this count to serious_start_count.
#4. Use the "$" character to count how many posts include the serious tag at the end of the title.
#Assign this count to serious_end_count.
#5. Use the "|" character to count how many posts include the serious tag at either the beginning or end of the title.
#Assign this count to serious_count_final.
    if re.search("[\[\(][sS]erious[\)\]]", record[0]) is not None:
        serious_count += 1
    if re.search("^[\[\(][sS]erious[\)\]]", record[0]) is not None:
        serious_start_count += 1
    if re.search("[\[\(][sS]erious[\)\]]$", record[0]) is not None:
        serious_end_count += 1
    if re.search("^[\[\(][sS]erious[\)\]]|[\[\(][sS]erious[\)\]]$", record[0]) is not None:
        serious_count_final += 1

print("1. Serious Count:", serious_count)
print("2. Serious Start Count:", serious_start_count)
print("3. Serious End Count:", serious_end_count)
print("4. Serious Count Final:", serious_count_final)
    #pass
