import csv

file_data = open("legislators.csv", "r")
legislators = list(csv.reader(file_data))
years = []
converted_years = []
for row in legislators[1:]:
    parts = row[2].split("-")
    years.append(parts[0])
for year in years:
    try:
        int(year)
    except:
        pass
    converted_years.append(year)
print(converted_years)
