import discord


async def help(message):
    if message.content.startswith('$help'):
        author = message.author.name+"#"+str(message.author.discriminator)
        print(message.author.name+"#"+str(message.author.discriminator))
        embedVar = discord.Embed(
            title="Help", description="Hello, @"+author+"! Here is how you can use this bot.", color=0x00ff00)
        embedVar.add_field(name="Generate an image using your imagination", value="First write `$ako` as command and then give an space and then write what you want to generate and send.\n Example:\
        ```\n$ako amazing city in space\n```", inline=False)

        embedVar.add_field(
            name="Black & White image to Colorful image", value="First write `$col` as command and then choose your photo from your computer that you want to colorize and send.\n Example:\
        ```\n$col\n [Upload your image]\n```", inline=False)

        embedVar.add_field(name="Full Page Webpage Capture",
                           value="First write `$wcap` as command and then give an space and put the website address without `http://` or `https://`.\n Example:\
        ```\n$wcap eliushhimel.com\n```", inline=False)

        embedVar.add_field(name="Photo background remover.",
                           value="First write `$bgx` as command and then choose your photo from your computer and send.\n Example:\
        ```\n$bgx\n [Upload your image]\n```", inline=False)

        embedVar.add_field(
            name="Get random cat and dog pictures.", value="First write `$cat` or  `$dog` and hit enter.\n Example:\
                \n- Cat```\n$cat\n``` \n - Dog ```\n$dog\n```", inline=False)

        embedVar.add_field(
            name="Search for free images from unsplash", value="First write `$upic` as command and then give an space and write what type of photo you want to search and send.\n Example:\
        ```\n$upic beautiful jungle\n```", inline=False)

        embedVar.add_field(name="Get random meme.", value="Frist write `$meme` and hit enter.\n Example:\
        ```\n$meme\n```", inline=False)

        # embedVar.add_field(name="Field1", value="hi", inline=False) #This is a template for new feature, copy and uncomment to use

        await message.reply(embed=embedVar)
