import requests
from decouple import config

API_KEY = config('API_KEY')


async def imgColorizer(message):
    # Image colorizer feature
    if 'chitrokar' or 'colorize' in message.channel.name:
        photoURL = message.attachments[0].url
        response = requests.post(
            "https://api.deepai.org/api/colorizer",
            data={
                'image': photoURL,
            },
            headers={'api-key': API_KEY}
        ).json()

        print(response)

        try:
            await message.reply(response['status'])

        except (KeyError, NameError, AttributeError) as e:
            await message.reply(response['output_url'])
