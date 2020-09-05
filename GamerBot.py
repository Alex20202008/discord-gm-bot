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


# events
@bot.event
async def on_ready():
	activity = discord.Activity(name='!!', type=discord.ActivityType.listening)
	await bot.change_presence(activity=activity)

@bot.event
async def on_member_join(user):
	channel_join = bot.get_channel(719185068349718598)
	await channel_join.send(f"{user.mention} зашел на сервер:)")


# commands

# START!!
bot.run(TOKEN)
