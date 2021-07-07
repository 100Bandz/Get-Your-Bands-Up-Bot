import asyncio
import discord
from discord import colour
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
import sys


logger = logging.getLogger('discord')   ##Error Logs are written to a file called discord.log
logger.setLevel(logging.DEBUG) 
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = "ODU5MjU3Mzk2Nzk3ODk4NzUy.YNqDzw.hLz7uunfA9btxDhx0kGNDvHEc1g"

bot = commands.Bot(command_prefix='>')
status = cycle(['AHHH','（。＾▽＾）','🤑🤑🤑','boolin'])

stockdict = {"gme": "GME", 'tesla': 'TSLA', "arkk": "ARKK", "aqn": "AQN", 'suncor' : 'SU.TO', "bitcoin": "BTC-USD", 'arkg': 'ARKG', 'arkx': 'ARKX'}


@bot.event
async def on_ready():
    change_status.start()
    # await bot.change_presence(status=discord.Status.online, activity=discord.Game("🤑🤑🤑"),afk=False)
    print("We have logged in as {0.user}".format(bot))
        # First get the channel where the message should be sent
    channel = discord.utils.get(bot.get_all_channels(), name='general')
    embed=discord.Embed(title="Bot is Online!", color= 0x03fcf0)
    embed.set_author(name= "Get Your Bands Up", icon_url=bot.user.avatar_url)
    await channel.send(embed=embed)

@bot.command()
async def start(ctx):
    starttime = time.time()
    while True:
        print("working :D")
        clr = "%06x" % random.randint(0, 0xFFFFFF)
        embed=discord.Embed(title="shmoney 🙏", description= 'The Bread comes first', color= 0x03fcf0)
        embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
        for kname, vtick in stockdict.items():
            stock_ticker = vtick
            stock_name = yf.Ticker(stock_ticker)
            marketprice = str(stock_name.info.get("regularMarketPrice", None))
            embed.add_field(name= stock_name.info.get("shortName"), value= '$'+ marketprice, inline=False)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/838242488598134796/862063340707643452/1624112952498.jpg')

        await ctx.send(embed=embed)
        await asyncio.sleep(120)


@tasks.loop(minutes= 5)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        embed=discord.Embed(title="Invalid Command used",color= discord.Colour.dark_red())
        embed.set_author(name= "Get Your Bands Up", icon_url=bot.user.avatar_url)
        await ctx.send(embed=embed)


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

@bot.command()
async def restart(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Restarting...", color= 0x03fcf0)
    embed.set_author(name= "Get Your Bands Up", icon_url=bot.user.avatar_url)
    message = await ctx.send(embed=embed)
    restart_program()


bot.run(TOKEN)