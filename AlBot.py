import discord

client = discord.Client()

# Loads token from file named token.txt
tokenFile = open('token.txt')
token = tokenFile.read()
tokenFile.close()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$move'):
        msgAuth = discord.utils.get(message.guild.members, name = message.author.name)
        if not msgAuth.voice:
            await message.channel.send("You're not in a voice channel.")
            return
        msgSpl = message.content.split(' ', 1)
        if len(msgSpl) == 1:
            await message.channel.send("Specify a channel to switch to.")
            return
        newChan = discord.utils.get(message.guild.voice_channels, name = msgSpl[1])
        if newChan is None:
            await message.channel.send("That channel doesn't exist.")
            return
        chMembs = msgAuth.voice.channel.members
        for mem in chMembs:
            await mem.move_to(newChan)

client.run(token)