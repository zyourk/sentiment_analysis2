import unittest


class MyTestCase(unittest.TestCase):
    def test_dreamcatcher(self):
        from analysis.lyric_grabber import get_lyrics_tester
        from analysis.sentiment_analyzer import analyze

        lyrics = get_lyrics_tester("radwimps", "nandemonaiya")
        result = analyze(lyrics)
        print(result)


if __name__ == '__main__':
    unittest.main()
