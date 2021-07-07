import asyncio
import discord
from discord import colour
from discord import message
from discord.embeds import Embed
from discord.ext import commands, tasks
import yfinance as yf
import pandas as pd
import numpy as np
import time
from asyncio.tasks import Task
import random
from discord import channel
import logging
import os
from itertools import cycle
import json
from datetime import datetime
import sys
import functools 

logger = logging.getLogger('discord')   ##Error Logs are written to a file called discord.log
logger.setLevel(logging.DEBUG) 
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = "ODU5MjU3Mzk2Nzk3ODk4NzUy.YNqDzw.hLz7uunfA9btxDhx0kGNDvHEc1g"

bot = commands.Bot(command_prefix='>')
status = cycle(['AHHH','（。＾▽＾）','🤑🤑🤑','boolin'])

stockdict = {"gme": "GME", 'tesla': 'TSLA', "arkk": "ARKK", "aqn": "AQN", 'suncor' : 'SU.TO', "bitcoin": "BTC-USD", 'arkg': 'ARKG', 'arkx': 'ARKX'}

def to_async(syncfunc):
    @functools.wraps(syncfunc)
    async def sync_wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        func = functools.partial(syncfunc, *args, **kwargs)
        return await loop.run_in_executor(None, func)

    return sync_wrapper


@bot.event
async def on_ready():
    change_status.start()
    # await bot.change_presence(status=discord.Status.online, activity=discord.Game("🤑🤑🤑"),afk=False)
    print("We have logged in as {0.user}".format(bot))
        # First get the channel where the message should be sent
    channel = discord.utils.get(bot.get_all_channels(), name='bot-spam')
    embed=discord.Embed(title="Bot is Online", color= 0x03fcf0)
    embed.set_author(name= "Get Your Bands Up", icon_url=bot.user.avatar_url)
    await channel.send(embed=embed)


@to_async
def getmarketdata_embed():
    print("working :D")
    embed=discord.Embed(title="shmoney 🙏", description= 'The Bread comes first', color= discord.Colour.random())
    for kname, vtick in stockdict.items():
        stock_ticker = vtick
        stock_name = yf.Ticker(stock_ticker)
        marketprice = str(stock_name.info.get("regularMarketPrice", None))
        embed.add_field(name= stock_name.info.get("shortName"), value= '$'+ marketprice, inline=False)
    return embed


@bot.command()
async def start(ctx):
    # while True:

    embed=discord.Embed(title="Getting your stocks ready! :)", description= 'Please wait...', color= 0x03fcf0)
    embed.set_author(name= "Get Your Bands Up", icon_url=bot.user.avatar_url)
    message = await ctx.send(embed=embed)

    while True:
        embed = await getmarketdata_embed()
        await ctx.send(embed=embed)


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