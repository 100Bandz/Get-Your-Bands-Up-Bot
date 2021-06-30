import discord
from discord.ext import commands

TOKEN = "ODU5MjU3Mzk2Nzk3ODk4NzUy.YNqDzw.hLz7uunfA9btxDhx0kGNDvHEc1g"

bot = commands.Bot(command_prefix='.')


@bot.event     ##Ctrl+K+C    Ctrl+K+U
async def on_ready():
    print("We have logged in as {0.user}".format(bot))



bot.run(TOKEN)