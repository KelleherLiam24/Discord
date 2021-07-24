import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="commands", description="Help page")
    async def _help(self,ctx):
        embed=discord.Embed(title="Commands", value=" ", color=0x695997)
        embed.add_field(name="Commands",value="!8ball\n!chance\n!coinflip\n!commands\n!hello\n!help\n!ping\n!price\n!tweet", inline=False)
        await ctx.send(embed=embed)