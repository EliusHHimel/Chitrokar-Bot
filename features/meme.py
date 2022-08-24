import requests

# get meme


async def getMeme(message):
    if message.content.startswith('$meme'):
        response = requests.get(
            'https://meme-api.herokuapp.com/gimme').json()
        print(response)
        await message.reply(response['url'])

