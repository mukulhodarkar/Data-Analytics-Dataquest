import csv
file_data = open("nfl-suspensions-data.csv", "r")
nfl_suspensions = list(csv.reader(file_data))

nfl_suspensions = nfl_suspensions[1:]
teams = []
games = []
for row in nfl_suspensions:
    team = row[1]
    teams.append(team)
    game = row[2]
    games.append(game)
#print(teams)
#print(games)
unique_teams = []
unique_games = []
unique_teams = set(teams)
unique_games = set(games)

print("teams:", unique_teams)
print("games:", unique_games)

#----------- better way ---------------
#teams = [row[1] for row in nfl_suspensions]
#unique_teams = set(teams)
#print(unique_teams)

#games = [row[2] for row in nfl_suspensions]
#unique_games = set(games)
#print(unique_games)
