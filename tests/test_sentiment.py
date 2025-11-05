import unittest


class MyTestCase(unittest.TestCase):
    def test_dreamcatcher(self):
        from analysis.lyric_grabber import get_lyrics_tester
        from analysis.sentiment_analyzer import analyze

        lyrics = get_lyrics_tester("boca", "dreamcatcher")
        result = analyze(lyrics)
        print(result)

    def test_multiple(self):
        from analysis.lyric_grabber import get_batched_lyrics
        from analysis.sentiment_analyzer import analyze

        songs = [
            {"song": "boca", "artist": "dreamcatcher"},
            {"song": "scream", "artist": "dreamcatcher"},
            {"song": "odd eye", "artist": "dreamcatcher"},
            {"song": "Butterfly", "artist": "BTS"},
            {"song": "Love Dive", "artist": "IVE"},
            {"song": "Pink Venom", "artist": "BLACKPINK"},
            {"song": "Attention", "artist": "NewJeans"},
            {"song": "ASAP", "artist": "STAYC"},
            {"song": "Savage", "artist": "aespa"},
            {"song": "Next Level", "artist": "aespa"},
            {"song": "Peaches", "artist": "Justin Bieber"},
            {"song": "Blinding Lights", "artist": "The Weeknd"},
            {"song": "Levitating", "artist": "Dua Lipa"},
            {"song": "Bad Habits", "artist": "Ed Sheeran"},
            {"song": "drivers license", "artist": "Olivia Rodrigo"},
        ]

        lyrics_map = get_batched_lyrics(songs)
        print("Fetched all lyrics")

        batch_lyrics = [lyrics_map[(s["song"], s["artist"])] for s in songs]

        results = analyze(batch_lyrics)
        print(results)


if __name__ == '__main__':
    unittest.main()
