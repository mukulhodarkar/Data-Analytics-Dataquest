#Problem:
#1. Create a class with an instance mwthod print_data(num_rows) which will print out data upto the given number of rows.
#2. Create an instance of that class and use it to print 5 rows from nfl.csv

#Solution:

#1. import CSV module. Purpose: File reading and splitting into a list of lists.
import csv

#2. Define a class, which has a method to print data
class Dataset:
    def __init__(self, data):
        self.data = data
    def print_data(self, num_rows):
        print(self.data[0:num_rows]) #self.data[] and not just self[]
#3. Open file into read mode
file_data = open("nfl.csv", "r")
#4. Read data from file, using reader method and convert the result into list
file_contents = list(csv.reader(file_data))
#5. Create an instance of dataset class.
nfl_data = Dataset(file_contents)

nfl_data.print_data(5)
