"""
Class for grabbing lyrics from songs using the lyricsgenius API
ref: https://github.com/johnwmillr/LyricsGenius
author: Zack Yourkavitch
"""

import os

from lyricsgenius import Genius
from dotenv import load_dotenv

load_dotenv()

genius = Genius(os.getenv("GENIUS_TOKEN"))
genius.verbose = False
genius.remove_section_headers = True


def get_lyrics():
    """
    Function to prompt user for artist and song & grab lyrics from result.
    :return: song lyrics.
    """
    artist = input("Enter Artist: ")
    song = input("Enter Song: ")
    song = genius.search_song(artist=artist, title=song)
    return song.lyrics

def get_lyrics_tester(artist, song):
    """
    Separate lyric grabbing function for testing get_lyrics().
    :param artist: The pre-defined artist.
    :param song: The pre-defined song.
    :return: song lyrics.
    """
    song = genius.search_song(artist=artist, title=song)
    return song.lyrics