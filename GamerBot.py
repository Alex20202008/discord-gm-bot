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
	activity = discord.Activity(name=' !!', type=discord.ActivityType.listening)
	await bot.change_presence(activity=activity)

@bot.event
async def on_member_join(user):
	channel_join = bot.get_channel(719185068349718598)
	await channel_join.send(f"{user.mention} зашел на сервер 🙂")

@bot.event
async def on_member_remove(user):
	channel_remove = bot.get_channel(719185068349718598)
	await channel_remove.send(f"{user.display_name} покинул сервер 😟")

# commands

@bot.command()
async def members(ctx):
	# member_count = len(ctx.guild.members)
	true_member_count = len([m for m in ctx.guild.members if not m.bot])
	await bot.send_message(f"На сервере {true_member_count} геймеров:)")

# START!!
bot.run(TOKEN)
