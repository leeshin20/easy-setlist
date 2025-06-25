# spotify_service.py

import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def search_track_info(title: str, artist: str):
    query = f"track:{title} artist:{artist}"
    result = sp.search(q=query, type='track', limit=1, market='JP')
    tracks = result.get('tracks', {}).get('items', [])
    if not tracks:
        # 검색 실패해도 기본 데이터 리턴
        return {
            "입력 제목": title,
            "입력 아티스트": artist,
            "검색된 제목": None,
            "검색된 아티스트": None,
            "앨범 커버": None  # 이미지 없음을 표시
        }

    track = tracks[0]
    return {
        "입력 제목": title,
        "입력 아티스트": artist,
        "검색된 제목": track['name'],
        "검색된 아티스트": track['artists'][0]['name'],
        "앨범 커버": track['album']['images'][0]['url']
    }