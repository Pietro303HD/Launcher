# bot.py
import os
import pyautogui
import json
from io import BytesIO
import discord

settings = json.load(open('settings.json'))

token = settings['token']
prefix = settings['prefix']

client = discord.Client()

@client.event
async def on_ready():
    print(
        f'https://discord.com/oauth2/authorize?client_id={client.user.id}'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == f'{prefix}move':
        response = 'testando'
        await message.channel.send(response)
    if message.content == f'{prefix}status':
        member = message.author
        embed = discord.Embed(title=f'{member.name} is', description= f'{member.activities[0].name}', color='GREEN')
    if message.content == f'{prefix}screenshot':
    	image = pyautogui.screenshot()
    	with BytesIO() as image_binary:
                    image.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await message.channel.send(file=discord.File(fp=image_binary, filename='image.png'))

client.run(token)
