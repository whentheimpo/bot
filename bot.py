from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

# Load environment variables from .env
load_dotenv()

# Get the token from the environment
token = os.getenv("DISCORD_TOKEN")

# Set up the bot
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run(token)
