
from discord.ext import commands
import requests
from requests import request
import discord
import os

from decouple import config

TOKEN = config('TOKEN')
API_KEY = config('API_KEY')

# token = os.getenv('TOKEN')
# apiKey = os.getenv('API_KEY')
print(TOKEN, API_KEY)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.content.startswith('$ako'):
            args = message.content.split('$ako ')
            query = args[1]

            response = requests.post('https://api.deepai.org/api/text2img',
                                     headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}, data={
                                         'text': {query},
                                     }).json()
            print(response)
            try:
                if (response['status']):
                    await message.reply(response['status'])

            except (KeyError, NameError, AttributeError) as e:
                await message.reply(response['output_url'])

            # else:
            #     await message.reply(response['output_url'])


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
