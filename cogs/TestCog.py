import discord
from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(hidden = True)
    @commands.is_owner()
    async def ownertest(self, ctx):
        await ctx.send('Yes')

def setup(bot: commands.Bot):
    bot.add_cog(TestCog(bot))