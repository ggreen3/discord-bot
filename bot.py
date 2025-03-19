import discord
import os
from discord.ext import commands

# Set up bot command prefix
intents = discord.Intents.default()
intents.messages = True  # Enable message intent

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot is online! Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}! 🤖')

TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # Read token from environment variable
bot.run(TOKEN)
