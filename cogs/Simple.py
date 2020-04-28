import discord
from discord.ext import commands
import random

class Simple(commands.Cog):
    """Simple features that everyone can use"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context):
        """Responds with \"Hello World!\""""
        await ctx.send('Hello World!')

    @commands.command()
    async def r6s(self, ctx: commands.Context):
        """Generates a search for a given user on R6Stats"""
        msgSpl = ctx.message.content.split(' ', 1)
        if len(msgSpl) == 1:
            await ctx.send("Specify user to look up")
            return
        await ctx.send("https://r6stats.com/search/" + msgSpl[1] + '/pc')

    @commands.command()
    async def roll(self, ctx: commands.Context):
        """Returns a random number from 1 to a given number."""
        msgSpl = ctx.message.content.split(' ')
        if len(msgSpl) == 1:
            await ctx.send("Specify a number.")
            return
        if not msgSpl[1].isdigit():
            await ctx.send("Not a valid number.")
            return
        maxsize = int(msgSpl[1])
        if maxsize == 0:
            await ctx.send("Not a valid number.")
            return
        await ctx.send('Rolled a {0}.'.format(random.randint(1,maxsize)))

def setup(bot: commands.Bot):
    bot.add_cog(Simple(bot))