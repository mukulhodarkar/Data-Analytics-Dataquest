import csv
file_data = open("nfl-suspensions-data.csv", "r")
nfl_suspensions = list(csv.reader(file_data))

nfl_suspensions = nfl_suspensions[1:]
years = {}
for row in nfl_suspensions:
    row_year = row[5]
    if row_year not in years:
        years[row_year] = 1
    else:
        years[row_year] += 1
print("years:", years)
