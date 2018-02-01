import csv

class Suspension:
    def __init__(self, data):
        self.data = data
        self.header = self.data[0]
        self.data = self.data[1:]
    def print_data(self, row_num):
        self.name = self.data[row_num][0]
        self.team = self.data[row_num][1]
        self.games = self.data[row_num][2]
        self.year = self.data[row_num][5]
        print(self.name, self.team, self.games, self.year)

file_data = open("nfl_suspensions_data.csv", "r")
nfl_suspensions = list(csv.reader(file_data))
third_suspension = Suspension(nfl_suspensions)
third_suspension.print_data(2)
