import csv

filename = open("nfl.csv", "r")
csvreader = csv.reader(filename)
nfl = list(csvreader)
#We can also use a one liner for above 2 steps: nfl = list(csvreader(filename))
#Loop through the dataset, counting rows with "New England Patriots" at 2nd index.
patriots_wins = 0
for record in nfl:
    if record[2] == "New England Patriots":
        patriots_wins += 1
print (patriots_wins)
