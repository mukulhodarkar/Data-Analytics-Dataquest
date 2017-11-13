import csv

class Dataset:
    def __init__(self, data):
        # during instatiation of the class object, we should now pass some data as a parameter.
        self.data = data

#open nfl.csv file in read mode
file_data = open("nfl.csv", "r")

#read data from file using CSV module's methods
nfl_data = list(csv.reader(file_data))

#Instantiate a new class object nfl_dataset and pass the file data as the paramenter
nfl_dataset = Dataset(nfl_data)

#access data using object parameter
dataset_data = nfl_dataset.data 
print(dataset_data)
