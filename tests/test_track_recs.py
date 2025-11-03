import unittest
import http.client

class MyTestCase(unittest.TestCase):
    def test_recs(self):
        from analysis.track_recs import return_recs
        result = return_recs(song="괜찮아!", artist="dreamcatcher")
        print(result)

    def test_recs2(self):
        from analysis.track_recs import return_recs
        result = return_recs(song="だから僕は音楽を辞めた", artist="yorushika")
        print(result)


if __name__ == '__main__':
    unittest.main()
