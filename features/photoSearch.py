import requests
from decouple import config

UNSPLASH_CLIENT_ID = config('UNSPLASH_CLIENT_ID')


async def searchPhoto(message):
    if message.content.startswith('$upic'):
        query = message.content.split('$upic ')[1]
        url = "https://api.unsplash.com//search/photos?query=" + \
            query
        photos = requests.get(url, headers={
            "Authorization": "Client-ID " + UNSPLASH_CLIENT_ID
        }).json()

        print(photos['results'])

        i = 0
        while i < 5:
            i += 1
            await message.reply("Photo by: " + photos['results'][i]['user']['name'] + ' on Unsplash')
            await message.reply(photos['results'][i]['urls']["full"])
