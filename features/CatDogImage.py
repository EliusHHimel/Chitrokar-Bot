import requests

# dog image search


async def dog(message):
    if message.content.startswith('$dog'):
        response = requests.get(
            'https://dog.ceo/api/breeds/image/random').json()
        print(response)
        await message.reply(response['message'])


# cat image search

async def cat(message):
    if message.content.startswith('$cat'):
        response = requests.get(
            'https://api.thecatapi.com/v1/images/search').json()
        print(response)
        await message.reply(response[0]['url'])
