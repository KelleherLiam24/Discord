import json
import requests

import discord
from discord.ext import commands

import Basic_Commands
import Stock_Price_Checker
import Help_Page
import Twitter_Bot


with open('config.json', 'r') as config:
    TOKEN = json.loads(config.read())['token']

description = ''' This is LiamBot '''
client = commands.Bot(command_prefix=commands.when_mentioned_or(
    "!"), description=description)


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='~~~~~~'))
    print('Logged in as')
    print(client.user.name)


if __name__ == "__main__":
    client.add_cog(Main(client))
    client.add_cog(Basic_Commands.Basic(client))
    client.add_cog(Stock_Price_Checker.Stock(client))
    client.add_cog(Help_Page.Help(client))
    client.add_cog(Twitter_Bot.Twitter(client))
    client.run(TOKEN)
