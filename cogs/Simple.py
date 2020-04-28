import discord
from discord.ext import commands
import random

class Simple(commands.Cog):
    """Simple features that everyone can use"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """Responds with \"Hello World!\""""
        await ctx.send('Hello World!')

    @commands.command()
    async def r6s(self, ctx, *, username):
        """Generates a search for a given user on R6Stats"""
        await ctx.send("https://r6stats.com/search/" + username + '/pc')

    @r6s.error
    async def r6s_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Specify user to look up.")

    @commands.command()
    async def roll(self, ctx, number: int):
        """Returns a random number from 1 to a given number."""
        if number < 1:
            raise commands.BadArgument
        await ctx.send('Rolled a {0}.'.format(random.randint(1,number)))

    @roll.error
    async def roll_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Specify a number.')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('Provide a number greater than 0.')

def setup(bot: commands.Bot):
    bot.add_cog(Simple(bot))