import csv

file_data = open("legislators.csv", "r")
legislators = list(csv.reader(file_data))
for row in legislators:
    birthday = row[2]
    birth_year = birthday.split("-")[0]
    try:
        birth_year = int(birth_year)
    except Exception:
        birth_year = 0
    row.append(birth_year) #appends birthyear at the end of each record.
print(legislators)
