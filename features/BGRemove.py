import requests
from decouple import config
import discord

BG_API_KEY = config('BG_API_KEY')


async def removeBG(message):
    if message.content.startswith('$bgx'):
        photoURL = message.attachments[0].url
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            data={
                'image_url': photoURL,
                'size': 'auto'
            },

            headers={'X-Api-Key': BG_API_KEY},
        )
        if response.status_code == requests.codes.ok:
            with open('no-bg.png', 'wb') as out:
                out.write(response.content)
                await message.reply(file=discord.File(out.name))
