from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

# Load environment variables from .env
load_dotenv()

# Get the token from the environment
token = os.getenv("DISCORD_TOKEN")

# Create intents to specify which events your bot will listen to
intents = discord.Intents.default()
intents.message_content = True  # Enables access to message content (if your bot needs it)

# Pass intents to the bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("ready to ban zaydeons"))

# Start the bot with the token
bot.run(token)
