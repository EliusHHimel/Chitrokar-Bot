import discord
from decouple import config
from discord.ext.commands import Bot
from discord.ext import commands

from features import Colorizer, Text2Img, CatDogImage, WebCapture, BGRemove, photoSearch, meme, Help


# Import private bot token from environment variable
TOKEN = config('TOKEN')


class MyClient(discord.Client):

    # Shows if the bot is ready to work in terminal
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        # Change the bot status
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='$help'))

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

        # Photo background remove
        await BGRemove.removeBG(message)

        # Get photo from unsplash
        await photoSearch.searchPhoto(message)

        # Get random meme
        await meme.getMeme(message)

        # Help command
        await Help.help(message)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)  # Run the client
