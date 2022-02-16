def getSkins():
    from mojang import MojangAPI
    import numpy as np
    import requests
    import shutil

    print('\nLoading Skins. . .')

    players = np.genfromtxt('players.txt', dtype='str', comments='#')

    for name in players:
        uuid = MojangAPI.get_uuid(name)
        print('Obtaining skin for', name)
        url = 'https://crafatar.com/avatars/{}'
        link = url.format(uuid)
        image = requests.get(link, stream=True)
        image.raw.decode_content = True
        path = '/Users/johnbeatty/PycharmProjects/teams/heads/{}'.format(name)
        with open(path, 'wb') as f:
            shutil.copyfileobj(image.raw, f)
