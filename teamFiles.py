from PIL import Image
import numpy as np

players = np.genfromtxt('players.txt', dtype='str', comments='#')

team1 = Image.open('/Users/johnbeatty/PycharmProjects/teams/template.jpg')
team2 = Image.open('/Users/johnbeatty/PycharmProjects/teams/template.jpg')
team3 = Image.open('/Users/johnbeatty/PycharmProjects/teams/template.jpg')
team4 = Image.open('/Users/johnbeatty/PycharmProjects/teams/template.jpg')

for skin in players:
    skin = Image.open('/Users/johnbeatty/PycharmProjects/teams/heads/{}'.format(skin))
    skin.show()