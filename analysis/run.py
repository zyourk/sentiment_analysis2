"""
needs to:
prompt user for artist and song
analyze & adjust song
print out sentiments
get best recommendation
print out best recommendation
"""
from track_algorithm import get_best_rec
if __name__ == "__main__":
    artist = input("Welcome to Sentiment Oriented Musical Assistance! Please name an artist to get started.\n")
    song = input("Great! Now name a song by that artist, and I'll get underway!\n")
    result_rec, result_sent = get_best_rec(artist=artist, song=song)
    print(f"The top emotion I'm detecting in your song is {result_sent['label']}. I'm {result_sent['score'] * 100}% sure of it!")
    print(f"I'm all done! If you like {song} by {artist}, I'm sure you'll like what I have for you here!")
    print(f"Try listening to {result_rec['song']} by {result_rec['artist']}!")