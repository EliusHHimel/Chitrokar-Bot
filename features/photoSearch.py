import requests
from decouple import config
import discord

UNSPLASH_CLIENT_ID = config('UNSPLASH_CLIENT_ID')


async def searchPhoto(message):
    if message.content.startswith('$upic'):
        query = message.content.split('$upic ')[1]
        url = "https://api.unsplash.com//search/photos?query=" + \
            query
        photos = requests.get(url, headers={
            "Authorization": "Client-ID " + UNSPLASH_CLIENT_ID
        }).json()

        i = 0
        while i < 5:
            i += 1
            embedVar = discord.Embed(
                title=None, description=None, color=0x552E12)

            embedVar.set_image(url=photos['results'][i]['urls']["raw"])
            embedVar.set_author(name=photos['results'][i]['user']['name'], url=photos['results'][i]['user']
                                ['links']['html'], icon_url=photos['results'][i]['user']['profile_image']['large'])
            await message.reply(embed=embedVar)

#"Photo by: "+'['+photos['results'][i]['user']['name']+']('+photos['results'][i]['user']['links']['html']+')'+' on [Unsplash](https://unsplash.com/)'
