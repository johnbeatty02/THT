#To Do List:
#autogenerate team pictures (discord api), Pillow (PIL) library
#Export team pictures to folders for easier image creation
#https://note.nkmk.me/en/python-pillow-paste/

import binpacking
import numpy as np

numberOfTeams = 4

levels = np.genfromtxt('points.txt', dtype = 'float')
players = np.genfromtxt('players.txt', dtype = 'str')
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

# calculates each team's average points
points1 = round(sum(team1[1])/4, 2)
points2 = round(sum(team2[1])/4, 2)
points3 = round(sum(team3[1])/4, 2)
points4 = round(sum(team4[1])/4, 2)

# calculates the standard deviation of each team
stDev1 = round(np.std(team1[1]), 2)
stDev2 = round(np.std(team2[1]), 2)
stDev3 = round(np.std(team3[1]), 2)
stDev4 = round(np.std(team4[1]), 2)

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
