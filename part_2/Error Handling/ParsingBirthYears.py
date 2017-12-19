#Create an empty list named birth_years.
#Loop through each item in legislators.
#Split the value in the birthday column on the - character.
#Assign the result to parts.
#Extract the first item in parts and append it to birth_years.
#At the end, birth_years will be a list containing the birth years of all the legislators in legislators

import csv

file_data = open("legislators.csv", "r")
legislators = list(csv.reader(file_data))

birth_years = []
for record in legislators[1:]:
    parts = record[2].split("-")
    birth_years.append(parts[0])
print(birth_years)
