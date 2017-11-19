#Read legislators.csv into the variable legislators, which is a list of lists.
#Extract the gender column from legislators and assign it to the variable gender.
#Convert gender to a set.

import csv

file_data = open("legislators.csv", "r")
legislators = list(csv.reader(file_data))
#print(legislators)

gender = []
for record in legislators[1:]:
    gender.append(record[3])

gender = set(gender)
print(gender)
