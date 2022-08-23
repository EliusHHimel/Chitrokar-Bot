import requests
from decouple import config

WEB_SS_API_KEY = config('WEB_SS_API_KEY')


async def webCap(message):
    if message.content.startswith('$wcap'):
        args = message.content.split('$wcap ')
        query = args[1]
        url = "https://shot.screenshotapi.net/screenshot?token="+WEB_SS_API_KEY + \
            "&url=https://"+query+"&full_page=true&output=json&file_type=png&wait_for_event=load"
        response = requests.get(url).json()

        try:
            await message.reply(response['screenshot'])

        except (KeyError, NameError, AttributeError) as e:
            await message.reply(response['error'])
