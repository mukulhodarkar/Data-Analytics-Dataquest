import csv
file_data = open("legislators.csv", "r")
legislators = list(csv.reader(file_data))

#Step 1: Get birthyear, append at the end of the file.
for row in legislators[1:]:
    birth_date = row[2]
    birth_year = birth_date.split("-")[0]
#convert birth_year to integer, and if NULL --> put 0
    try:
        birth_year = int(birth_year)
    except Exception:
        birth_year = 0
#Append at the end of each record.
    row.append(birth_year)

#Step 2: Check for gender and birth_year
# Put names and
name_counts = {}
for row in legislators[1:]:
    gender = row[3]
    birth_year = row[7]
    if gender == 'F' and birth_year > 1940:
        # Get the first name of the legislator
        name = row[1]
        # Check if that name exists in the dictionary,
        # if present --> increment its count, else --> Set count as 1
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

#Step 3: Check for count == 2, append the name in the top_female_names[] list.
top_female_names = []

for name, count in name_counts.items():
    if count == 2:
        top_female_names.append(name)

print("Most common female names amongst legislators from 1940:", top_female_names)
