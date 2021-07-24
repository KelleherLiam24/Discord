import discord
from discord.ext import commands
import requests
import bs4

class Stockx(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="stockxprice", description = "Checks price on stockX")
    async def _stockxprice(self, ctx, item):
        