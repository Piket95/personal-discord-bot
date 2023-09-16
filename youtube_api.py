import json
import os

import pytz
import requests
from dateutil import parser

YOUTUBE_API_BASE_URL = 'https://youtube.googleapis.com/youtube/v3'
YOUTUBE_BASE_VIDEO_URL = 'https://www.youtube.com/watch?v='
MAX_PLAYLIST_RESULTS = 1  # need only one. if the video id isn't the saved one the queried one is newer


def check_genshin_yt_channel():
    GENSHIN_IMPACT_PLAYLIST_ID = os.getenv('GENSHIN_IMPACT_SONDERSENDUNG_PL_ID')

    savedJsonData = None

    # get saved yt video id from saved json file or set predefined layout if file doesn't exist
    try:
        with open('data/saved_yt_video_id.json', 'r') as f:
            savedJsonData = json.load(f)
    except Exception as error:
        print('An exception has occurred: ', error)

    if savedJsonData is None:
        savedJsonData = {
            'lastSavedVideoId': ''
        }

    parameter = {
        'part': 'snippet,contentDetails',
        'playlistId': GENSHIN_IMPACT_PLAYLIST_ID,
        'maxResults': MAX_PLAYLIST_RESULTS,
        'key': os.getenv('YT_API_KEY')
    }

    headers = {
        'Accept': 'application/json'
    }

    response = requests.get(YOUTUBE_API_BASE_URL + '/playlistItems', params=parameter, headers=headers)
    data = response.json()
    newestVideoId = data['items'][0]['contentDetails']['videoId']
    videoDate = data['items'][0]['snippet']['publishedAt']

    message = False

    if savedJsonData['lastSavedVideoId'] != newestVideoId:
        savedJsonData['lastSavedVideoId'] = newestVideoId

        formattedVideoDate = (parser.parse(videoDate).astimezone(pytz.timezone('Europe/Berlin'))
                              .strftime('%d.%m.%Y, %H:%M:%S'))

        urlToPost = YOUTUBE_BASE_VIDEO_URL + newestVideoId
        message = f'Neue Sondersendung vom **{formattedVideoDate} Uhr**\n{urlToPost}'

    with open('data/saved_yt_video_id.json', 'w') as f:
        f.write(json.dumps(savedJsonData, indent=4))

    return message
