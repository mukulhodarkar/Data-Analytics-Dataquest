import csv

file_data = open("legislators.csv", "r")
legislators = list(csv.reader(file_data))

#Step 1: Get birth year from birthdate and append the year in the given csv data.

#Separate the birth year from given birthdaySo it can be used to compare in the next loop with the value 1940.
for row in legislators:
    birthday = row[2]
    birth_year = birthday.split("-")[0]
    try:
        birth_year = int(birth_year)
    except Exception:
        birth_year = 0
    #append birthyear at the end of each record.
    row.append(birth_year)

# step 2: Use conditions to check gender and birth year and
#        Put the names in name_counts dictionary and increment the count.

name_counts = {}
for row in legislators:
    gender = row[3]
    year = row[7]
    # Dont use this --> if row[3] == 'F' and row[7] > 1940: as it might confuse the reader.
    #instead assign these values to appropriately named variables and then use those variables in the program.
    if gender == 'F' and year > 1940:
        name = row[1]
        if name in name_counts:
            name_counts[name] = name_counts[name] + 1
        else:
            name_counts[name] = 1
#print(name_counts)
# Now name_counts is a dictionary where the keys are female first names from legislators,
# and the values are the number of times the names occured after 1940

# Step 3: determine the highest totals in name_counts
# Assign the value associated with the key to count.
# If max_value is None, or count is greater than max_value:
# Assign count to max_value.
max_value = None
for row in name_counts:
    count = name_counts[row]
    if(max_value is None or max_value < count):
         max_value = count
              
print  ("The Highest Female Name count is", max_value)
