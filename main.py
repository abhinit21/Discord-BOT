import os

from discord.ext import commands

# from .settings import *

bot = commands.Bot(command_prefix='!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and filename != '__init__.py':
        bot.load_extension(f'cogs.{filename[:-3]}')

DISCORD_BOT_TOKEN = 'NzYwNzc0NjgxOTI5NzExNjQ3.X3Q8og.BLj-VLJBzHS-WcAh0SfAZdl6ihQ'

print('Logged on as {0}!'.format(bot.user))
bot.run(DISCORD_BOT_TOKEN)
