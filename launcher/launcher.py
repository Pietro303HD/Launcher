import requests
import json
local = {
"launcher": 0.0
"pcbot": 0.0
}

version = requests.get('https://raw.githubusercontent.com/Pietro303HD/Launcher/master/versions.json')
print("Nothing to see here.")
for app, ver in version.json():
    print(f'{app} : {ver}')
    if ver > local[app]:
        print(f'{app} needs a update!')
