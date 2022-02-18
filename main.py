#To Do List:
# Integrate Discord API:
#    create bot
#    automatically read names from "me" channel
# Find better sorting algorithm / read through stackoverflow suggestions
# put all teams in one exported image with head and name labels
# Amend to include only players who are playing in a specific week
# Do something with the Player, Points header -- get rid of it or add it to sheets integration

import binpacking
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skins import getSkins

numberOfTeams = 4

# CHANGE THIS TO txt OR csv
extension = 'csv'
name = 'wobtafitv'
filename = name + '.' + extension

if extension == 'txt':
    levels = np.genfromtxt('points.txt', dtype='float')
    players = np.genfromtxt('players.txt', dtype='str')
elif extension == 'csv':
    df = pd.read_csv(filename)
    df.columns = ['Players', 'Points']
    players = list(df.Players)
    levels = list(df.Points)
else:
    raise ValueError('Invalid extension, options are \'csv\' or \'txt\'.')

if name == 'pvp':
    pass

playerLevels = zip(players, levels)
playerLevelsList = list(playerLevels)

averageLevels = sum(levels)/len(levels)

print('Generating', numberOfTeams, 'teams with a player count of', len(players)/numberOfTeams, 'and an average of', round(averageLevels, 2), 'points each...')

bins = binpacking.to_constant_bin_number(playerLevelsList, numberOfTeams, 1)

a, b, c, d = [[individualArray] for individualArray in bins]

# reads players into an array
a = a[0]
b = b[0]
c = c[0]
d = d[0]

# converts the arrays to lists
team1 = list(zip(*a))
team2 = list(zip(*b))
team3 = list(zip(*c))
team4 = list(zip(*d))

team1Points = list(team1[1])
team2Points = list(team2[1])
team3Points = list(team3[1])
team4Points = list(team4[1])
allPoints = [team1Points, team2Points, team3Points, team4Points]

# calculates each team's average points
points1 = round(sum(team1Points)/4, 2)
points2 = round(sum(team2Points)/4, 2)
points3 = round(sum(team3Points)/4, 2)
points4 = round(sum(team4Points)/4, 2)

# calculates the standard deviation of each team
stDev1 = round(np.std(team1Points), 2)
stDev2 = round(np.std(team2Points), 2)
stDev3 = round(np.std(team3Points), 2)
stDev4 = round(np.std(team4Points), 2)

# prints results
print('Team 1 is', team1[0])
print('Team 2 is', team2[0])
print('Team 3 is', team3[0])
print('Team 4 is', team4[0])
print('\n-----Stats-----')
print('Team 1 Average is', points1, 'with a standard deviation of', stDev1)
print('Team 2 Average is', points2, 'with a standard deviation of', stDev2)
print('Team 3 Average is', points3, 'with a standard deviation of', stDev3)
print('Team 4 Average is', points4, 'with a standard deviation of', stDev4)

# graphs!
labels = ['Team 1', 'Team 2', 'Team 3', 'Team 4']
fig, ax =plt.subplots()
ax.set_title('Points by Team')
data = np.array(allPoints, dtype = 'object')
x = np.arange(data.shape[0])
ax.set_ylabel('Points')

for i in range(data.shape[1]):
    bottom=np.sum(data[:,0:i], axis=1)
    ax.bar(labels,data[:,i], bottom=bottom, label="Team {}".format(i+1))
plt.show()

#getSkins() # from skins.py, obtains skin images and routes to /Users/johnbeatty/PycharmProjects/teams/heads
