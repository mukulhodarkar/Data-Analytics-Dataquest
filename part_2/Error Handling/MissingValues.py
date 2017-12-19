#focus on populating empty fields with a specified value.
#Step by step, we:
#Loop through each row in rows.
#Check whether the party column (index 6) has a missing value.
#If so, replace it with the string No Party.
#For gender, replace any missing values with the string M.


import csv

file_data = open("legislators.csv", "r")
legislators = list(csv.reader(file_data))

gender = []
party = []

for row in legislators[1:]:
    if row[6] == "":
        row[6] = "No Party"
    if row[3] == "":
        row[3] = "M"
    gender.append(row[3])
    party.append(row[6])


gender = set(gender)
party = set(party)

print(gender)
print(party)
