import json
import os
import sys

import pytz
import requests
from dateutil import parser

YOUTUBE_API_BASE_URL = 'https://youtube.googleapis.com/youtube/v3'
YOUTUBE_BASE_VIDEO_URL = 'https://www.youtube.com/watch?v='
MAX_PLAYLIST_RESULTS = 1  # need only one. if the video id isn't the saved one the queried one is newer


def load_playlist_config() -> dict:

    playlistConfig = {}

    try:
        with open('config/yt-video-feeds.json', 'r') as f:
            playlistConfig = json.load(f)
    except FileNotFoundError:
        print('\033[91mFehler: Die Config-Datei unter "config/yt-video-feeds.json" fehlt!\033[0m')
        sys.exit()

    return playlistConfig


def check_for_new_yt_videos():

    playlistConfig = None
    savedJsonData = {}

    # load playlist config
    playlistConfig = load_playlist_config()

    # get saved yt video id from saved json file or set predefined layout if file doesn't exist
    try:
        with open('data/saved_yt_video_id.json', 'r') as f:
            savedJsonData = json.load(f)
    except Exception as error:
        if not isinstance(error, FileNotFoundError):
            print(f'\033[91mAn exception has occurred: {error}\033[0m')

    queriedVideos = []

    if bool(playlistConfig) and 'playlistFeeds' in playlistConfig:
        for playlistFeed in playlistConfig['playlistFeeds']:
            if playlistFeed['skip']:
                continue

            parameter = {
                'part': 'snippet,contentDetails',
                'playlistId': playlistFeed['playlistId'],
                'maxResults': playlistFeed['maxPlaylistResults'],
                'key': os.getenv('YT_API_KEY')
            }

            headers = {
                'Accept': 'application/json'
            }

            response = requests.get(YOUTUBE_API_BASE_URL + '/playlistItems', params=parameter, headers=headers)
            data = response.json()
            newestVideoId = data['items'][0]['contentDetails']['videoId']
            videoDate = data['items'][0]['snippet']['publishedAt']

            queriedVideos.append({
                'name': playlistFeed['name'].replace(" ", "-").lower(),
                'playlistName': playlistFeed['name'].replace(" ", "-").lower(),
                'videoId': newestVideoId,
                'videoDate': videoDate,
                'destDCChannelId': playlistFeed['destinationDCChannelId']
            })

    messageObj = []

    if bool(queriedVideos):

        for video in queriedVideos:

            if not video['name'] in savedJsonData:
                savedJsonData[video['name']] = {}

            if ('lastSendVideoId' not in savedJsonData[video['name']]
                    or savedJsonData[video['name']]['lastSendVideoId'] != video['videoId']):

                savedJsonData[video['name']]['lastSendVideoId'] = video['videoId']

                formattedVideoDate = (parser.parse(video['videoDate']).astimezone(pytz.timezone('Europe/Berlin'))
                                      .strftime('%d.%m.%Y, %H:%M:%S'))

                urlToPost = YOUTUBE_BASE_VIDEO_URL + video['videoId']

                messageObj.append({
                    'playlistName': video['playlistName'],
                    'url': urlToPost,
                    'destDCChannelId': video['destDCChannelId'],
                    'videoDate': formattedVideoDate
                })

    with open('data/saved_yt_video_id.json', 'w') as f:
        f.write(json.dumps(savedJsonData, indent=4))

    return messageObj
