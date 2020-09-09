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
	channel_rulus = bot.get_channel(718152214547267654)
	channel_join = bot.get_channel(719185068349718598)
	chat = bot.get_channel(718170421559558196)
	await channel_join.send(f"{user.mention}, приветствую на сервере 🙂\nОбязательно прочитай правила в {channel_rulus.mention} и приступай к общению в {chat.mention}")

@bot.event
async def on_member_remove(user):
	channel_remove = bot.get_channel(719185068349718598)
	await channel_remove.send(f"{user.mention} покинул(а) сервер 😟")



# commands
@bot.command()
async def members(ctx):
    member_count = len(ctx.guild.members) # includes bots
    await ctx.send(f"На сервере **{member_count}** участников!")


@bot.command()
async def avatar(ctx, member: discord.Member):
	author = ctx.message.author
	embed = discord.Embed( description='**Аватарка пользователя ' + str(member.mention) + '**', colour=discord.Colour.blue())
	embed.set_image(url=member.avatar_url)

	await ctx.send(embed=embed)


# START!!
bot.run(TOKEN)