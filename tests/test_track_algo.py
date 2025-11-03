import unittest


class MyTestCase(unittest.TestCase):
    def test_boca(self):
        from analysis.track_algorithm import get_best_rec
        result = get_best_rec(song="BOCA", artist="Dreamcatcher", debug=True)
        print(result)

    def test_eternal_sunshine(self):
        from analysis.track_algorithm import get_best_rec
        result = get_best_rec(song="Eternal Sunshine", artist="Flower Face", debug=True)
        print(result)

    def test_ditto(self):
        from analysis.track_algorithm import get_best_rec
        result = get_best_rec(song="DITTO", artist="Aries", debug=True)
        print(result)

    def test_og_song_no_feat(self):
        from analysis.track_algorithm import get_best_rec
        result = get_best_rec(song="2 months", artist="UAU", debug=True)
        print(result)


if __name__ == '__main__':
    unittest.main()
