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
    def column_unique(self, label):
        unique_list = set(self.column(label))    #this combines following two steps: Step1: column_values_list = self.column(label)  Step2: unique_count = set(column_values_list)
        return len(unique_list)                 #return unique_list this returns a set, if we want to return a count as an int, then calculate it's length here and return the length i.e. count itself

#------------------------ class defination ends-----------------------

file_data = open("nfl.csv", "r")
file_contents = list(csv.reader(file_data))
nfl_data = Dataset(file_contents)
total_years = nfl_data.column_unique('year')
print(total_years)
