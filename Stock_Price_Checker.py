import discord
from discord.ext import commands
import requests
import bs4
import argparse
from collections import OrderedDict



class Stock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="price", description="checks stock price")
    async def _price(self, ctx, ticker):
        url = "https://finance.yahoo.com/quote/"

        full_url = url + ticker
        stock_graph = "https://stockcharts.com/c-sc/sc?s=" + ticker + "&p=D&b=5&g=0&i=0&"

        response = requests.get(full_url).content

        soup = bs4.BeautifulSoup(response, 'html.parser')

        stock_name = soup.findAll(class_="D(ib) Fz(18px)", attrs={"data-reactid": "7"})[0].text
        stock_price = soup.findAll(class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")[0].text
        if soup.findAll(class_="Ta(end) Fw(600) Lh(14px)", attrs={"data-test": "FIFTY_TWO_WK_RANGE-value"}):
            stock_52week = soup.findAll(class_="Ta(end) Fw(600) Lh(14px)", attrs={"data-test": "FIFTY_TWO_WK_RANGE-value"})[0].text
        else:
            stock_52week = "N/A"
        if soup.findAll(class_="Ta(end) Fw(600) Lh(14px)", attrs={"data-test": "MARKET_CAP-value"}):
            stock_marketCap = soup.findAll(class_="Ta(end) Fw(600) Lh(14px)", attrs={"data-test": "MARKET_CAP-value"})[0].text
            cap = "Market Cap: "
        elif soup.findAll(class_="Ta(end) Fw(600) Lh(14px)", attrs={"data-test": "NET_ASSETS-value"}):
            stock_marketCap = soup.findAll(class_="Ta(end) Fw(600) Lh(14px)", attrs={"data-test": "NET_ASSETS-value"})[0].text
            cap = "Net Assets: "
        else:
            stock_marketCap = "N/A"
            cap = "Market Cap: "
        
        embed=discord.Embed(title=stock_name, color=0x695997)
        embed.add_field(name="Stock Price: ", value=stock_price, inline=True)
        embed.add_field(name="52-Week Range: ", value=stock_52week, inline=True)
        embed.add_field(name=cap, value=stock_marketCap, inline=True)
        embed.set_image(url=stock_graph)
        embed.set_footer(text=f"StockChecker")
        await ctx.send(embed=embed)
