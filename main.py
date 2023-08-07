from logging import Logger
import discord
from discord.ext import commands
import config
from discord import app_commands
from logger import setup_logger
import typing
import helps


bot = commands.Bot(command_prefix="FDGghfd8g4gifdjk", help_command=None, intents=discord.Intents.all())
logger: Logger = setup_logger()
tree = app_commands.CommandTree(bot)


@bot.event
async def on_ready():
    await tree.sync(guild=config.GUILD_OBJECT)
    logger.info("Ready!")

@tree.command(name = "info", description = "Generate graph with some fun info", guild=config.GUILD_OBJECT)
@app_commands.describe(channel="Used only for \"message\"", member="Used only for \"message\"", mode="Choose \"help\" to see info about modes")
async def info(
        interaction: discord.Interaction, 
        mode: typing.Literal["help", "joins", "leaves", "joins/leaves", "message"],
        channel: typing.Optional[discord.TextChannel] = None,
        member: typing.Optional[discord.Member] = None
):
    if any((channel, member)) and mode != "message":
        return await interaction.response.send_message(
            "channel and member params is only used with \"message\"\n"
            "You shouldn't use it with other modes", ephemeral=True)

    match mode:
        case "help":
            return await interaction.response.send_message(helps.info, ephemeral=True)
        case "joins":
            pass
        case "leaves":
            pass
        case "joins/leaves":
            pass
        case "message":
            pass


bot.run(config.TOKEN)
