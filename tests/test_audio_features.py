import unittest

class MyTestCase(unittest.TestCase):
    def test_get_features(self):
        import analysis.audio_features as features
        result = features.get_audio_features("emotion", "dreamcatcher")
        print(result)

    def test_more_features(self):
        import analysis.audio_features as features
        result = features.get_audio_features("spring thief", "yorushika")
        print(result)

if __name__ == '__main__':
    unittest.main()
