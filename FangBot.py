# This program is free software and licensed under the GNU Affero General Public License verson 3 (AGPL)
# The AGPL can be found in the LICENSE file within this repository
# Alternatively, the AGPL can be found here: https://www.gnu.org/licenses/agpl-3.0.en.html

import os
import logging
from datetime import timedelta
from random import randrange

import discord
from discord.ext import commands as dc

# Perform some configuration for our application.
botToken = os.getenv("TOKEN")
intents = discord.Intents.all()
bot = dc.Bot(command_prefix="!", intents=intents)
logger = logging.getLogger('discord')

# Remove the built in help command so that we can define a custom help command.
bot.remove_command("help")

@bot.event
async def on_ready():
    logger.info(f"{bot.user.name} is ready.")

@bot.command()
async def sneed(ctx):
    await ctx.send("What you s*need* are your meds, Anon.")
    member = ctx.author
    startingDelta = timedelta(days=1, minutes=1)
    totalSeconds = startingDelta.total_seconds()
    chosenSecondsAmount = randrange(1, totalSeconds)
    formattedChosenSecondsAmount = format(str(timedelta(seconds=chosenSecondsAmount)))
    logger.info(formattedChosenSecondsAmount)
    await member.timeout(startingDelta)

@bot.command()
async def info(ctx):
    message = """
FangBot has been developed by
- BobCzar
- rc_05

Other developers will be added when needed.
The source code is available [here](https://github.com/BobCzar/FangBot).
"""
    await ctx.send(message)

@bot.command()
async def help(ctx):
    message = """
All commands must start with !
List of commands:
- sneed
    Sneed's Feed & Seed (Formerly Chuck's)
- help
    This very message that you are seeing.
- info
    Extra info that you may or may not find interesting.
"""
    await ctx.send(message)

bot.run(botToken)
