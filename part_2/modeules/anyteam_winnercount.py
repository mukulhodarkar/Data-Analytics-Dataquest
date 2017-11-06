import csv

def nfl_wins(team_name):
    #open file in read mode
    filename = open("nfl.csv", "r")
    #use csv module methods to read the file in a list
    #convert the result in the form of a list
    nfl = list(csv.reader(filename))
    team_wins = 0
    for record in nfl:
        if record[2] == team_name:
            team_wins += 1
    return team_wins

cowboys_wins = nfl_wins("Dallas Cowboys")
falcons_wins = nfl_wins("Atlanta Falcons")
print("Cowboys wins:", cowboys_wins)
print("Falcons wins:", falcons_wins)
