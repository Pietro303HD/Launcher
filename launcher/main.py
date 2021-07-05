import requests
import json

from install import update

local = json.load(open('../versions.json',))
version = requests.get('https://raw.githubusercontent.com/Pietro303HD/Launcher/master/versions.json')

print(local)
print(version.json())
for app, ver in version.json().items():
    print(f'{app} : {ver}')
    if ver > local[app]:
        print(f'{app} needs a update!')
        update(app)
