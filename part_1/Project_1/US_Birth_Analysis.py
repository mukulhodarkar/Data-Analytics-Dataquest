
# coding: utf-8

# # U.S. Births Data Analysis

# U.S. Births Data from 1994 to 2003.
#
# year -->	Year
# month -->	Month
# date_of_month -->	Day number of the month
# day_of_week -->	Day of week, where 1 is Monday and 7 is Sunday
# births -->	Number of births

def read_csv(file_name):
    f = open(file_name, "r")
    data = f.read()
    birth_data = {}
    string_list = data.split('\r') #the file's records are not separated on a new line character \n. Instead it happened to be separated by a \r character.7
    final_list = []
    int_fields = []
    for record in string_list[1:len(string_list)]:
        string_fields = record.split(',')
        int_fields = list(map(int, string_fields))
        final_list.append(int_fields)
    print('-----------')
    return final_list



def calculate_births(input_list, day_of_week):
    for each in input_list:
        if each[3] == day_of_week:
            day_births = day_births + int(each[4])
    #return day_births
    for record in clean_data[1:len(clean_data)]:
        day_of_week = record[3]
        num_births = int(record[4])
        if day_of_week in birth_data:
            birth_data[day_of_week] = birth_data[day_of_week] + num_births
        else:
            birth_data[day_of_week] = num_births
    print(birth_data)


cdc_list = read_csv("births.csv")

print(cdc_list[0:10])
