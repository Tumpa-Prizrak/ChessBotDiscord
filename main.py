from contextlib import suppress
from logging import Logger
import discord
from discord.ext import commands
import config
from discord import app_commands
from logger import setup_logger
import typing


bot = commands.Bot(command_prefix="FDGghfd8g4gifdjk", help_command=None, intents=discord.Intents.all())
logger: Logger = setup_logger()
tree = app_commands.CommandTree(bot)


@bot.event
async def on_ready():
    logger.info("Ready!")

@tree.command(name = "info", description = "Generate graph with some fun info", guild=discord.Object(id=config.GUILD_ID))
async def first_command(
        interaction: discord.Interaction, 
        mode: typing.Literal["help", "joins", "leaves", "joins/leaves", "message"], 
        channel: typing.Optional[discord.TextChannel] = None
):
    pass


bot.run(config.TOKEN)
