import discord
import random

client = discord.Client()

# Loads token from file named token.txt
tokenFile = open('token.txt')
token = tokenFile.read()
tokenFile.close()

# Loads help dialog from commands.txt
commandsFile = open('commands.txt')
commands = commandsFile.read()
commandsFile.close()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot:
        return
    # Command List
    # Command: $help
    if message.content.startswith('$help'):
        await message.channel.send(commands)
    # Hello World
    # Command: $hello
    if message.content.startswith('$hello'):
        await message.channel.send('Hello World!')

    # Move people in current voice channel to new channel 
    # Command: $move <Voice Channel>
    if message.content.startswith('$move'):
        msgAuth = message.author
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

    # Split users in current voice channel into teams
    # Command: $team
    if message.content.startswith('$team'):
        msgAuth = discord.utils.get(message.guild.members, name = message.author.name)
        if not msgAuth.voice:
            await message.channel.send("You're not in a voice channel.")
            return
        chMembs = msgAuth.voice.channel.members
        random.shuffle(chMembs)
        memName = [m.mention for m in chMembs]
        teamA = memName[len(memName) // 2:]
        teamB = memName[:len(memName) // 2]
        await message.channel.send('Team 1: ' + ' '.join(teamA))
        await message.channel.send('Team 2: ' + ' '.join(teamB))
client.run(token)