import discord
from discord.ext import commands
import youtube_dl
import Checks

class MusicPlayer(commands.Cog):

    @commands.command()
    @Checks.in_voice()
    async def join(self, ctx):
        pass

    @commands.command()
    @Checks.in_voice()
    async def leave(self, ctx):
        pass
    
    @commands.command()
    @Checks.in_voice()
    async def play(self, ctx, *, url: str):
        pass

    @commands.command()
    @Checks.in_voice()
    async def pause(self, ctx):
        pass

    @commands.command()
    @Checks.in_voice()
    async def queue(self, ctx, *, url: str):
        pass

    @commands.command()
    @Checks.in_voice()
    async def remove(self, ctx, *, index: int):
        pass