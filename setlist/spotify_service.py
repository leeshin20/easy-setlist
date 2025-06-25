import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

auth_manager = SpotifyClientCredentials(client_id = CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def search_track_info(title: str):
    result = sp.search(q=title, type='track', limit=1)
    tracks = result.get('tracks', {}).get('items', [])
    if not tracks:
        return None
    
    track = tracks[0]
    return {
        'title': track['name'],
        'artist': track['artists'][0]['name'],
        'image_url': track['album']['images'][0]['url']
    }

if __name__ == "__main__":
    info = search_track_info("beyond the time")
    print(info)