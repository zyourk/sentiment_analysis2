"""
Class for grabbing lyrics from songs using the lyricsgenius API
ref: https://github.com/johnwmillr/LyricsGenius
author: Zack Yourkavitch
"""

import os
from concurrent.futures import ThreadPoolExecutor

from lyricsgenius import Genius
from dotenv import load_dotenv
import analysis.translator as translator

load_dotenv()

genius = Genius(os.getenv("GENIUS_TOKEN"))
genius.verbose = False
genius.timeout = 7
genius.remove_section_headers = True


def get_lyrics():
    """
    Function to prompt user for artist and song & grab lyrics from result.
    :return: song lyrics.
    """
    artist = input("Enter Artist: ")
    song = input("Enter Song: ")
    result = genius.search_song(artist=artist, title=song)
    if result and translator.check_english(result.lyrics):
        return result.lyrics
    if result and not translator.check_english(result.lyrics):
        english_search = genius.search_song(artist=artist, title=f"{song} english translation")
        if english_search.lyrics:
            return english_search.lyrics
        else:
            return translator.translate(result.lyrics)
    else:
        return "Sorry, I was unable to find that song."

def get_lyrics_tester(song, artist, debug=False):
    """
    Separate lyric grabbing function for testing get_lyrics().
    :param artist: The pre-defined artist.
    :param song: The pre-defined song.
    :return: song lyrics.
    """
    result = genius.search_song(artist=artist, title=song)
    if result and translator.check_english(result.lyrics):
        return result.lyrics
    if result and not translator.check_english(result.lyrics):
        english_search = genius.search_song(artist=artist, title=f"{song} english translation")
        if english_search and english_search.lyrics:
            return english_search.lyrics
        else:
            if debug:
                print(translator.translate(result.lyrics))
            return translator.translate(result.lyrics)
    else:
        return "Sorry, I was unable to find that song."

def get_batched_lyrics(songs):
    results = {}
    with ThreadPoolExecutor(max_workers=15) as executor:
        for (song_artist, lyrics) in executor.map(fetch_lyrics, [(s["song"], s["artist"]) for s in songs]):
            results[song_artist] = lyrics
        return results

def fetch_lyrics(song_tuple):
    song, artist = song_tuple
    return (song, artist), get_lyrics_tester(song, artist)