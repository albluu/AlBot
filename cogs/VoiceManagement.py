import discord
from discord.ext import commands
import random


class VoiceManagement(commands.Cog):
    """Contains features for managing users in voice channels"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def move(self, ctx):
        """Moves users to a new voice channel (case sensitive)"""
        msgAuth = ctx.author
        if not msgAuth.guild_permissions.move_members:
            await ctx.send("You don't have permission to move people.")
            return
        if not msgAuth.voice:
            await ctx.send("You're not in a voice channel.")
            return
        msgSpl = ctx.message.content.split(' ', 1)
        if len(msgSpl) == 1:
            await ctx.send("Specify a channel to switch to.")
            return
        newChan = discord.utils.get(ctx.guild.voice_channels, name = msgSpl[1])
        if newChan is None:
            await ctx.send("That channel doesn't exist.")
            return
        chMembs = msgAuth.voice.channel.members
        for mem in chMembs:
            await mem.move_to(newChan)
    
    @commands.command()
    async def team(self, ctx):
        """Generates two teams based on members in the current voice channel"""
        msgAuth = ctx.author
        if not msgAuth.voice:
            await ctx.send("You're not in a voice channel.")
            return
        chMembs = msgAuth.voice.channel.members
        random.shuffle(chMembs)
        memName = [m.mention for m in chMembs]
        teamA = memName[len(memName) // 2:]
        teamB = memName[:len(memName) // 2]
        await ctx.send('Team 1: ' + ' '.join(teamA))
        await ctx.send('Team 2: ' + ' '.join(teamB))

    @commands.command()
    async def group(self, ctx):
        """Pulls all users in voice channels into a specified channel"""
        msgAuth = ctx.author
        if not msgAuth.guild_permissions.move_members:
            await ctx.send("You don't have permission to move people.")
            return
        if not msgAuth.voice:
            await ctx.send("You're not in a voice channel.")
            return
        msgSpl = ctx.message.content.split(' ', 1)
        if len(msgSpl) == 1:
            await ctx.send("Specify a channel to group into.")
            return
        newChan = discord.utils.get(ctx.guild.voice_channels, name = msgSpl[1])
        if newChan is None:
            await ctx.send("That channel doesn't exist.")
            return
        voiceChan = ctx.guild.voice_channels
        chMembs = []
        for chan in voiceChan:
            if chan is not newChan:
                chMembs += chan.members
        for mem in chMembs:
            await mem.move_to(newChan)

    @commands.command()
    async def eject(self, ctx):
        """Leave the voice channel, in style."""
        if ctx.author.voice:
            await ctx.send(':crab: {0} is gone :crab:'.format(ctx.author.mention))
            await ctx.author.move_to(None)

def setup(bot: commands.Bot):
    bot.add_cog(VoiceManagement(bot))