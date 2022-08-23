import requests
from decouple import config

API_KEY = config('API_KEY')


async def text2img(message):
    # Image colorizer feature
    if message.content.startswith('$ako'):
        args = message.content.split('$ako ')
        query = args[1]

        response = requests.post('https://api.deepai.org/api/text2img',
                                 headers={'api-key': API_KEY}, data={
                                     'text': {query},
                                 }).json()
        print(response)

        # Try if it shows an error then it will show the error message, otherwise it will show the output
        try:
            await message.reply(response['status'])

        except (KeyError, NameError, AttributeError) as e:
            await message.reply(response['output_url'])
