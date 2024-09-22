from datetime import datetime
import os

import discord
import pytz
from discord.ext import tasks

import youtube_api


class DiscordBot(discord.Client):

    async def setup_hook(self) -> None:
        self.check_for_new_yt_videos.start()

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        print(f'Message from {message.author}: {message.content}')

    @tasks.loop(hours=6)
    async def check_for_new_yt_videos(self):
        now = datetime.now(pytz.timezone('Europe/Berlin'))

        print(f'[{now.strftime("%d.%m.%y, %H:%M:%S")}] Checking for new YouTube Videos')

        messageObj = youtube_api.check_for_new_yt_videos()

        rolesToPing = '@everyone'

        if messageObj:
            for message in messageObj:
                text = (f'||{ rolesToPing }||\nNeue Sondersendung vom **{ message["videoDate"] } '
                           f'Uhr** aus der Playlist "{ message["playlistName"] }"\n{ message["url"] }')

                if os.getenv('ENV') is 'prod':
                    destDCChannel = self.get_channel(int(message['destDCChannelId']))
                else:
                    destDCChannel = self.get_channel(int(os.getenv('BOT_TEST_CHANNEL_ID')))

                await destDCChannel.send(text)

    @check_for_new_yt_videos.before_loop
    async def before_yt_check(self):

        await self.wait_until_ready()
