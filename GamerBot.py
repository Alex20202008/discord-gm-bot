# setup
import discord
from discord.ext import commands
import random
import os


# important
TOKEN = os.environ.get('TOKEN') # no u
prefix = "!!"
bot = commands.Bot(command_prefix = prefix)
bot.remove_command("help")


# when online
@bot.event
async def on_ready():
	activity = discord.Activity(name='!!', type=discord.ActivityType.listening)
	await bot.change_presence(activity=activity)


# commands



# START!!
bot.run(TOKEN)
