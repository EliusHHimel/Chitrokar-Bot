from email.mime import image
import requests
import discord
from decouple import config

from features import Colorizer, Text2Img

# Import private bot token and api key from environment variable
TOKEN = config('TOKEN')
API_KEY = config('API_KEY')

print(Colorizer)


class MyClient(discord.Client):

    # Shows if the bot is ready to work in terminal
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    # Get message from user and react to the command
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        # print('--------------------')
        # print(message)
        # print('--------------------')
        # print(message.attachments[0].url)
        # print('--------------------')

        # Generate text 2 image

        await Text2Img.text2img(message)
        # Image colorizer feature
        await Colorizer.imgColorizer(message)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)  # Run the client
