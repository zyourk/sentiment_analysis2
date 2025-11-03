import unittest


class MyTestCase(unittest.TestCase):
    def test_dreamcatcher(self):
        from analysis.sentiment_algorithm import get_sentiments

        modified, original = get_sentiments(song="괜찮아!", artist="dreamcatcher")
        print(f"original: {original}")
        print(f"modified: {modified}")


if __name__ == '__main__':
    unittest.main()
