import csv

file_data = open("legislators.csv", "r")
legislators = list(csv.reader(file_data))
for row in legislators[1:]:
    birthday = row[2]
    birth_year = birthday.split("-")[0]
    try:
        birth_year = int(birth_year)
    except Exception:
        birth_year = 0
    row.append(birth_year) #appends birthyear at the end of each record.

last_value = 1
print(legislators[0:10])
for record in legislators[1:]:
    if record[7] == 0:
        record[7] = last_value
    last_value = record[7]
counter = 1
for row in legislators:
    print(legislators[counter][7])
    counter += 1
