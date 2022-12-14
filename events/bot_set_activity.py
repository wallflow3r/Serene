import random
from settings.config import settings
import discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix=settings['prefix'], case_insensitive=True, intents=discord.Intents.all())
bot.remove_command('help')


@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
    if interaction:
        return
    if error:
        return


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="/help"))
    await change_presence.start()


@tasks.loop(minutes=30)
async def change_presence():
    rand_num = random.randint(1, 3)
    if rand_num == 1:
        await bot.change_presence(activity=discord.Game(name="/help"))
    if rand_num == 2:
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name=f"за {len(bot.guilds)} серверами"))
    if rand_num == 3:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"за котиками"))


bot.run(settings['token'])
