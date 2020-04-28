import discord
from discord.ext import commands

# Load token from token.txt
tokenFile = open('token.txt')
token = tokenFile.read()
tokenFile.close()

bot = commands.Bot(
    command_prefix = '$',
    activity = discord.Game(name = 'Commands: $help'),
    case_insensitive=True
)

bot.load_extension('cogs.BotManagement')
#bot.load_extension('cogs.Simple')
bot.load_extension('cogs.VoiceManagement')

bot.run(token)
print('Bot is running')