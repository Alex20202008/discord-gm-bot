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
	pass


# commands
@bot.command()
async def bruh(ctx):
	await ctx.send("bruuuuh")


# START!!
bot.run(TOKEN)