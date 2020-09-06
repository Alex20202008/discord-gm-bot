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
    member_count = len(ctx.guild.members) # includes bots
    await ctx.send(f"На сервере **{member_count}** участников!")


@bot.command()
async def avatar(ctx, member: discord.Member):
	sendAvatar = discord.Embed(
		color = discord.Color.blue()
	)
	sendAvatar.set_image(url={}.fromat(member.avatar_url))
	await ctx.send(sendAvatar)


# START!!
bot.run(TOKEN)