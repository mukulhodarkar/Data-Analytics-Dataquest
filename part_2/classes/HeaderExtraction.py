#You may have noticed when printing the data that the first element in the list of rows contains some header information.
#Using the csv module, we don't have a way of extracting this header unless we grab the first element.
#However, with our dataset class, we could add an instance method that would grab the first result of self.data,
#set it as a header attribute, and then remove it from the data attribute.


#Problem
#1. Add the extract_header() code to the initializer and set the header data to self.header.
#2. Create a variable called nfl_header and set it to the header attribute

import csv

class Dataset:
    def __init__(self, data):
        self.data = data
#         def extract_header(self): Do not declare another function, You have to do the header computation in the __init__ fuction itself.
        self.header = self.data[0]  #get header data
        self.data = self.data[1:]

file_data = open("nfl.csv", "r")
file_contents = list(csv.reader(file_data))
nfl_data = Dataset(file_contents)
nfl_header = nfl_data.header

print("nfl header:", nfl_header)
