from email.mime import image
import discord
from decouple import config

from features import Colorizer, Text2Img, CatDogImage, WebCapture

# Import private bot token from environment variable
TOKEN = config('TOKEN')


class MyClient(discord.Client):

    # Shows if the bot is ready to work in terminal
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    # Get message from user and react to the command
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        # Generate text 2 image
        await Text2Img.text2img(message)

        # Image colorizer feature
        await Colorizer.imgColorizer(message)

        # search random dog and cat image
        await CatDogImage.dog(message)
        await CatDogImage.cat(message)

        # Web Capture
        await WebCapture.webCap(message)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)  # Run the client
