import json
import os
from datetime import datetime

import discord
import pytz
from discord.ext import tasks

import youtube_api


class DiscordBot(discord.Client):

    genshinNewsChannel: discord.channel.TextChannel

    async def setup_hook(self) -> None:
        self.check_genshin_yt_channel.start()

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        # get genshin news channel object
        self.genshinNewsChannel = self.get_channel(int(os.getenv('GENSHIN_IMPACT_NEWS_CHANNEL_ID')))

    async def on_message(self, message):
        if message.author == self.user:
            return

        print(f'Message from {message.author}: {message.content}')

    @tasks.loop(hours=6)
    async def check_genshin_yt_channel(self):
        now = datetime.now(pytz.timezone('Europe/Berlin'))

        print(f'[{now.strftime("%d.%m.%y, %H:%M:%S")}] Checking genshin yt channel')

        message = youtube_api.check_genshin_yt_channel()

        if message:
            await self.genshinNewsChannel.send(message)

    @check_genshin_yt_channel.before_loop
    async def before_yt_check(self):

        await self.wait_until_ready()
