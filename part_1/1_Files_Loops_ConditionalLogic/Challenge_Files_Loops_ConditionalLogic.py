f = open('dq_unisex_names.csv', 'r')
names = f.read()
names = names.split('\n')
nested_list = []
for name in names:
    record = name.split(',')
    nested_list.append(record)

numerical_list = []
temp_list = []
for name in nested_list[:len(nested_list)-1]:     #since the last element is an empty space, it was trhowing error for index out of range.
    person_name = name[0]
    total_person = float(name[1])

    temp_list = [person_name, total_person]     #Place a record as a pair. If you put to separately, then they no longer will be connected to each other. They will simply be 2 different strings in the same list.

    numerical_list.append(temp_list)            #TEMP_LIST CONTAINS ONLY 1 RECORD AT A TIME.

#print(numerical_list[:5])
#print(type(numerical_list))

#The data set contains first names shared by at least 100 people. Let's limit it those shared by at least 1,000 people.
#Create a new list of strings called thousand_or_greater that only contains the names shared by 1,000 people or more.
thousand_or_greater = []
for line in numerical_list:
    if line[1] > 1000:
        thousand_or_greater.append(line[0]) #append Name to the list
print(thousand_or_greater)
