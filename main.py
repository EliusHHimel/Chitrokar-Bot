import requests
import discord
from decouple import config

# Import private bot token and api key from environment variable
TOKEN = config('TOKEN')
API_KEY = config('API_KEY')


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
        # print(message.type)
        # print('--------------------')

        # Generate text 2 image
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


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)  # Run the client
