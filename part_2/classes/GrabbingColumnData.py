#Add a method named column that takes in a label argument, finds the index of the header, and returns a list of the column data.
#If the label is not in the header, you should return None.
#Create a variable called year_column and set it to the return value of column('year').
#Create a variable called player_column and set it to the return value of column('player').


import csv

class Dataset:
    def __init__(self, data):
        self.data = data
        self.header = data[0]
        self.data = self.data[1:]
    def column(self, label):
#if label is not present in header, return none
        if label not in self.header:
            return None
#Now, label is present in the header. So lets find the index of the label i.e. header's index
#save_index is used to save the index generated from enumerate
        save_index = 0
        for index, element in enumerate(self.header):
            if label == element:
                save_index = index
#Now we have found out the index at which the label is. Print the data which resides at the given index in the column.
        column_values = []
        for row in self.data:
            column_values.append(row[save_index])
        return column_values

file_data = open("nfl.csv", "r")
file_contents = list(csv.reader(file_data))
nfl_data = Dataset(file_contents)
year_column = nfl_data.column('year')
player_column = nfl_data.column('player')
print("Years:", year_column, "Players:", player_column)
