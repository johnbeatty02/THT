#To Do List:
#make .exe file
#integrate google docs
#autogenerate team pictures (discord api), Pillow (PIL) library

#Export team pictures to folders for easier image creation
#https://note.nkmk.me/en/python-pillow-paste/

import binpacking
import numpy as np

#database of past points

levels = np.genfromtxt('points.txt', dtype = 'float')
players = np.genfromtxt('players.txt', dtype = 'str')
playerLevels = zip(players, levels)
playerLevelsList = list(playerLevels)

averageLevels = sum(levels)/len(levels)
print('Average points are', averageLevels)

bins = binpacking.to_constant_bin_number(playerLevelsList, 4, 1)

a, b, c, d = [ [individualArray] for individualArray in bins]

a = a[0]
b = b[0]
c = c[0]
d = d[0]
a1 = a[1]
b1 = b[1]
c1 = c[1]
d1 = d[1]

team1 = list(zip(*a))
team2 = list(zip(*b))
team3 = list(zip(*c))
team4 = list(zip(*d))

points1 = sum(team1[1])/4
points2 = sum(team2[1])/4
points3 = sum(team3[1])/4
points4 = sum(team4[1])/4

stdev1 = np.std(team1[1])
stdev2 = np.std(team2[1])
stdev3 = np.std(team3[1])
stdev4 = np.std(team4[1])

print('Team 1 is', team1[0])
print('Team 2 is', team2[0])
print('Team 3 is', team3[0])
print('Team 4 is', team4[0])
print('\n-----Stats-----')
print('Team 1 Average is', points1, 'with a standard deviation of', stdev1)
print('Team 2 Average is', points2, 'with a standard deviation of', stdev2)
print('Team 3 Average is', points3, 'with a standard deviation of', stdev3)
print('Team 4 Average is', points4, 'with a standard deviation of', stdev4)
