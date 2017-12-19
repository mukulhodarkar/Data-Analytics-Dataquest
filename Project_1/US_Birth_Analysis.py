
# coding: utf-8

# # U.S. Births Data Analysis

# U.S. Births Data from 1994 to 2003.
#
# year -->	Year
# month -->	Month
# date_of_month -->	Day number of the month
# day_of_week -->	Day of week, where 1 is Monday and 7 is Sunday
# births -->	Number of births

def calculate_births(input_list, day_of_week):
    for each in input_list:
        if each[3] == day_of_week:
            day_births = day_births + int(each[4])
    return day_births

f = open("births.csv", "r")
data = f.read()
#print(data)
birth_data = {}
split_data = data.split('\r') #the file's records are not separated on a new line character \n. Instead it happened to be separated by a \r character.
clean_data = []
print(split_data[0:5])
for record in split_data:
    details = record.split(',')
    clean_data.append(details)
print('-----------')
print(clean_data[0:5])
for record in clean_data[1:len(clean_data)]:
    day_of_week = record[3]
    num_births = int(record[4])
    if day_of_week in birth_data:
        birth_data[day_of_week] = birth_data[day_of_week] + num_births
    else:
        birth_data[day_of_week] = num_births
print(birth_data)
