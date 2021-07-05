import requests
import json

def update(app):
	# get all filenames on a folder
	# rewrite/write them all.
	for file in requests.get(f'https://api.github.com/repos/Pietro303HD/Launcher/contents/{app}/').json():
		path = file['path']
		open(f'../{path}', 'w').write(requests.get(file['download_url']).text)
	print(f'{app} has been updated!')
	vers = json.load(open('../versions.json'))
	vers[app] = requests.get('https://raw.githubusercontent.com/Pietro303HD/Launcher/master/versions.json')[app]
	versw = open(f'../versions.json', 'w')
	versw.write(json.dumps(vers))
	
