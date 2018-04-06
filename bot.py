import json
import discord
import requests
from discord.ext import commands

TOKEN = 'NDMxODgwMjM0MDYxNTI5MTAx.DalUUQ.YEVgbJYBBCjwxHXEDYFZ7p9yaD8'
discord_url="https://discordapp.com/api"

description = '''JibixBot in Python'''
bot = commands.Bot(command_prefix='#', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def user(name):
    req=requests.get('https://api.tibiadata.com/v2/characters/'+name+'.json')
    json_data = json.loads(req.text)
    await bot.say(json_data["characters"]["data"]["level"])
    await bot.say(json_data["characters"]["other_characters"][0])
@bot.command()
async def hello():
    """Says world"""
    await bot.say("world")


@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

bot.run(TOKEN)

