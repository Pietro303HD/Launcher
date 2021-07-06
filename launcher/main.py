import requests
import json

from install import update

print(
'   ___ _      _                 __                        _               '
'  / _ (_) ___| |_ _ __ ___     / /  __ _ _   _ _ __   ___| |__   ___ _ __ '
' / /_)/ |/ _ \ __| '__/ _ \   / /  / _` | | | | '_ \ / __| '_ \ / _ \ '__|'
'/ ___/| |  __/ |_| | | (_) | / /__| (_| | |_| | | | | (__| | | |  __/ |   '
'\/    |_|\___|\__|_|  \___/  \____/\__,_|\__,_|_| |_|\___|_| |_|\___|_|   '
'                                                                          '  
)

local = json.load(open('../versions.json',))
version = requests.get('https://raw.githubusercontent.com/Pietro303HD/Launcher/master/versions.json')

print(local)
print(version.json())
for app, ver in version.json().items():
    print(f'{app} : {ver}')
    if ver > local[app]:
        print(f'{app} needs a update! Would you like to update it?')
        prompt = input('> ')
        if promp == 'y': update(app)
            
while True:
    cmd = input('> ')
