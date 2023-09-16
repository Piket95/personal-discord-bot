from dotenv import load_dotenv
import os
import requests


def check_genshin_yt_channel():
    YOUTUBE_API_BASE_URL = 'https://youtube.googleapis.com/youtube/v3'
    GENSHIN_IMPACT_PLAYLIST_ID = 'PLqWr7dyJNgLJrcB0p96Q_yJHa_GLpPBq9'

    parameter = {
        'part': 'snippet,contentDetails',
        'playlistId': GENSHIN_IMPACT_PLAYLIST_ID,
        'maxResults': 3,
        'key': os.getenv('YT_API_KEY')
    }

    headers = {
        'Accept': 'application/json'
    }

    response = requests.get(YOUTUBE_API_BASE_URL + '/playlistItems', params=parameter, headers=headers)

    print(response.json())


if __name__ == '__main__':
    load_dotenv()
    check_genshin_yt_channel()
