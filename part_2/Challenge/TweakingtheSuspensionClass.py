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
        print(self.name, self.team, self.games, self.year)

    def get_year(self, row_num):
        try:
            self.year = int(self.data[row_num][5])
        except Exception:
            self.year = 0
            return (self.year)
        #print("Year:", self.year)

#----------------------------- Class definition ends -------------------

file_data = open("nfl_suspensions_data.csv", "r")
nfl_suspensions = list(csv.reader(file_data))
suspension = Suspension(nfl_suspensions)
twenty_third_year = suspension.get_year(22)
print(twenty_third_year)
