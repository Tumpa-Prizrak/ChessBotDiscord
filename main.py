from contextlib import suppress
from logging import Logger
import discord
from discord.ext import commands
import config
from discord import app_commands
from logger import setup_logger


bot = commands.Bot(command_prefix="FDGghfd8g4gifdjk", help_command=None, intents=discord.Intents.all())
logger: Logger = setup_logger()

@bot.event
async def on_ready():
    print("Ready!")

bot.run(config.TOKEN)
