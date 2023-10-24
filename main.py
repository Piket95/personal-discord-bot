import os

import discord
from dotenv import load_dotenv

from discord_bot import DiscordBot

if __name__ == '__main__':

    # load all env variables from .env file
    print('Loading .env file...')
    load_dotenv()

    # discord bot
    print('Starting discord bot...')

    intents = discord.Intents.default()
    intents.message_content = True

    # self in DiscordBot Class is now in the bot variable
    bot = DiscordBot(intents=intents)
    bot.run(os.getenv('DISCORD_BOT_TOKEN'))
