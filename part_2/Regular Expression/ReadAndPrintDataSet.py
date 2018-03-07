import csv

class Dataset(object):
    def __init__(self, data):
        self.data = data
        posts_with_header = self.data
        self.header = self.data[0]
        self.data = self.data[1:]
    def print_data(self,num_rows):
        print(self.data[:num_rows])



# ------------ Class definition ends -------------

file_contents = open("reddit_2015.csv", "r", encoding="utf8")
file_data = list(csv.reader(file_contents))
reddit_data = Dataset(file_data)
reddit_data.print_data(10)
