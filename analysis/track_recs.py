from dotenv import load_dotenv
import os, requests

load_dotenv()

lfm_key = os.getenv('LAST_FM_KEY')
lfm_app = os.getenv('APP_NAME')

url = "https://ws.audioscrobbler.com/2.0/"

def get_recs(artist, song):
    headers = {
        "User-Agent": lfm_app,
    }

    params = {
        "method": "track.getSimilar",
        "api_key": lfm_key,
        "artist": artist,
        "track": song,
        "limit": 15,
        "format": "json"
    }

    response = requests.get(url, headers=headers, params=params)
    try:
        response.raise_for_status()
        data = response.json()
        if (not "similartracks" in data) or (not data["similartracks"]["track"]):
            return {
                "error": "No similar tracks found",
            }
        return [
            {
                "name": t["name"],
                "artist": t["artist"]["name"],
                "url": t["url"]
            }
            for t in data["similartracks"]["track"]
        ]
    except Exception as e:
        return {
            "error": str(e),
        }

def return_recs(song, artist):
    recs = get_recs(song=song, artist=artist)
    if 'error' in recs:
        print("No recs")
        return None
    formatted = []
    for rec in recs:
        formatted.append({
            'song': rec["name"],
            'artist': rec["artist"],
        })
    return formatted