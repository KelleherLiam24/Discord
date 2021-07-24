from discord.ext import commands 
from random import seed
from random import randint
import emoji

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hello", description="hello world")
    async def _hello(self, ctx):
        try:
            await ctx.send("Hello!")
        except ValueError:
            await ctx.send("Unknown Command")
    @commands.command(name="ping", description="pong")
    async def _ping(self, ctx):
        try:
            await ctx.send("Pong")
        except ValueError:
            await ctx.send("Unknown Command")
    @commands.command(name="chance", description="chancecalc")
    async def _how(self, ctx, *args):
        em = [':grimacing:', ':laughing:', ':flushed:', ':sleeping:', ':angry:', ':cry:', ':sweat:', ':grinning:', ':unamused:', ':open_mouth:', ':anguished:', ':joy:']
        emVal = randint(0, len(em)-1)
        face = em[emVal]
        value = randint(0,100)
        await ctx.send(f"There is a {value}% chance " + " ".join(args[:]) +  " " + emoji.emojize(face, use_aliases=True))
    @commands.command(name="coinflip", description="flips a coin")
    async def _coinflip(self,ctx):
        value = randint(0,1)
        if(value == 1):
            await ctx.send("It's Tails!")
        elif(value == 0):
            await ctx.send("It's Heads!")
    @commands.command(name="8ball", description="8ball")
    async def _8ball(self,ctx, *args):
        responses = [' As I see it, yes.', 'Ask again later.', 'Better not tell you now.', 'Don’t count on it.', 'It is certain.', 'It is decidedly so.',
         'Most likely.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Outlook good.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.',
         'Yes.', 'Yes – definitely.']
        eightval = randint(0, len(responses)-1)
        await ctx.send(responses[eightval])
