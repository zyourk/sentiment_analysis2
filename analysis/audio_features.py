import os
from dotenv import load_dotenv
import requests, base64, json
import urllib.parse

load_dotenv()

id = os.getenv("SPOTIFY_ID")
secret = os.getenv("SPOTIFY_SECRET")
AUDIO_FEATURE_KEYS = {
    'acousticness','danceability','energy','instrumentalness','key',
    'liveness','loudness','mode','speechiness','tempo','valence'
}

def get_token():
    auth_str = id + ":" + secret
    auth_bytes = auth_str.encode("utf-8")
    auth_b64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_b64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    return json_result["access_token"]

token = get_token()

def get_song_id(song, artist, token=token, limit=10):
    headers = {"Authorization": "Bearer " + token}
    base = "https://api.spotify.com/v1/search"
    q = f'track:"{song}" artist:"{artist}"'
    q_enc = urllib.parse.quote_plus(q)
    url = f"{base}?q={q_enc}&type=track&limit={limit}"

    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    items = resp.json().get("tracks", {}).get("items", [])

    if not items:
        raise ValueError(f"No Spotify search results for: {song} - {artist}")

    artist_lower = artist.strip().lower()
    song_lower = song.strip().lower()
    for t in items:
        artist_names = [a["name"].strip().lower() for a in t["artists"]]
        if artist_lower in artist_names:
            if t["name"].strip().lower() == song_lower:
                return t["id"]
            candidate_id = t["id"]
            candidate = t

    for t in items:
        if t["name"].strip().lower() == song_lower:
            return t["id"]

    if 'candidate_id' in locals():
        return candidate_id
    return items[0]["id"]


def get_audio_features(song, artist):
    song_id = get_song_id(song, artist)

    url = f"https://api.reccobeats.com/v1/audio-features?ids={song_id}"

    payload = {}
    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    try:
        response.raise_for_status()
        json = response.json()
        content = json.get("content", [])
        if content:
            return {k: content[0][k] for k in content[0].keys() if k in AUDIO_FEATURE_KEYS}
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
