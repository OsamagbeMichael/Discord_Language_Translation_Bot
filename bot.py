from discord.ext import commands
import discord
import os 
from dotenv import load_dotenv

bot_key = os.getenv('BOT_TOKEN')

load_dotenv()

CHANNEL_ID = 1284633390032883742

bot = commands.Bot(command_prefix= "!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello! Lets get this!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! Study bot is ready!")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(bot_key)