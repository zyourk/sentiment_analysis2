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
    artist = input("Welcome to Sentiment Oriented Musical Assistance (v2.0)! Please name an artist to get started.\n")
    song = input("Great! Now name a song by that artist, and I'll get underway!\n")
    result_same_rec, result_diff_rec, result_sent = get_best_rec(artist=artist, song=song)
    if not(result_same_rec or result_diff_rec or result_sent):
        print("""
        Did you type your artist and song correctly?
        If so, unfortunately, it appears the song you selected is unsupported in my database.
        Spotify has deprecated many of their API features, so newer projects for the same purposes are upheld by small, often unpaid teams.
        Please try again with a different song.""")
    else:
        print(f"The top emotion I'm detecting in your song is {result_sent['label']}. I'm {(result_sent['score'] * 100):.2f}% sure of it!\n")
        print(f"I'm all done! If you like {song} by {artist}, I'm sure you'll like what I have for you here!")
        print(f"Want a song from the same artist? You should listen to \"{result_same_rec['song']}\"!")
        print(f"If you're looking for someone new, try out \"{result_diff_rec['song']}\" by {result_diff_rec['artist']}!\n")
        print("Please give your opinions on your experience in this survey:")
        print("https://docs.google.com/forms/d/e/1FAIpQLSc59ZMR_au2alE3dtjoSpHptKZl9NE3OldFKNinRymreregtg/viewform?usp=dialog")