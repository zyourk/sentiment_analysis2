import unittest


class MyTestCase(unittest.TestCase):

    def test_lyrics(self):
        """
        Very simple test to check if the lyrics function works as expected.
        More tests to be added for fault tolerance.
        :return: pass if lyrics are expected.
        """
        import analysis.lyric_grabber as lyric
        lyrics = lyric.get_lyrics_tester(artist="the champs", song="tequila")
        assert(lyrics == "Tequila\n\nTequila\n\nTequila")

if __name__ == '__main__':
    unittest.main()
