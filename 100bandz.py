import discord
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.bot import BotBase
import yfinance as yf
import pandas as pd
import numpy as np
import time
from asyncio.tasks import Task
from typing import AnyStr
import random
from discord import channel
from discord.ext import commands, tasks
import logging
import os
from itertools import cycle
import json
from datetime import datetime


logger = logging.getLogger('discord')   ##Error Logs are written to a file called discord.log
logger.setLevel(logging.DEBUG) 
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = "ODU5MjU3Mzk2Nzk3ODk4NzUy.YNqDzw.hLz7uunfA9btxDhx0kGNDvHEc1g"

bot = commands.Bot(command_prefix='.')



@bot.event     ##Ctrl+K+C    Ctrl+K+U
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    # StockInfo(stockdict)

@bot.command()
async def embed(ctx):
    starttime = time.time()
    while True:
        print("working :D")
        # msft = yf.Ticker("MSFT")
        # print(msft.info)
        embed=discord.Embed(title="Bandz To Make Her Dance", url="https://realdrewdata.medium.com/", description= 'The Bread comes first', color=0xFF5733)
        embed.set_author(name= ctx.author.display_name , url="https://twitter.com/RealDrewData", icon_url= ctx.author.avatar_url)
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/838242488598134796/861778628533813248/1624112952498.jpg')
        for kname, vtick in stockdict.items():
            stock_ticker = vtick
            stock_name = yf.Ticker(stock_ticker)
            marketprice = stock_name.info.get("regularMarketPrice", None)
            embed.add_field(name= stock_name.info.get("shortName"), value= marketprice, inline=False)

        await ctx.send(embed=embed)
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))


@bot.command()
@commands.is_owner()
async def Stop(ctx):
    embed = discord.Embed(title="Bot has been shutdown", color=0xFF5733) #Issue: the bot is doing the embed command and wont do anything else until it finishes
    await ctx.send(embed=embed)
    await ctx.bot.logout()
    # bot.run_coroutine_threadsafe(ctx.bot.logout(), ctx.bot.loop)      ##Fix this 


stockdict = {"GME": "gme", "ARKK": "ark", "TEC.TO": "tec.to", "AQN": "aqn"}


# def StockInfo(stock_dict):
#     starttime = time.time()
#     while True:
#         print("working :D")
#         for kname, vtick in stock_dict.items():
#             stock_ticker = vtick
#             stock_name = yf.Ticker(stock_ticker)
#             # print(stock_name.info)

#             marketprice = stock_name.info.get("regularMarketPrice", None)
#             print(marketprice)
#         time.sleep(60.0 - ((time.time() - starttime) % 60.0))

bot.run(TOKEN)