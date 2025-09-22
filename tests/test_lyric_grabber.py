import unittest


class MyTestCase(unittest.TestCase):

    def test_simple_lyrics(self):
        """
        Very simple test to check if the lyrics function works as expected.
        More tests to be added for fault tolerance.
        :return: pass if lyrics are expected.
        """
        import analysis.lyric_grabber as lyric
        lyrics = lyric.get_lyrics_tester(artist="the champs", song="tequila")
        assert(lyrics == "Tequila\n\nTequila\n\nTequila")

    def test_more_lyrics(self):
        """
        Testing more complex lyrics than... Tequila (also I love Dreamcatcher).
        Indentation is messed up because of strict string equality testing.
        :return: pass if lyrics are expected.
        """
        import analysis.lyric_grabber as lyric
        lyrics = lyric.get_lyrics_tester(artist="dreamcatcher", song="bonvoyage farewell ver")
        assert(lyrics == """(Ooh) Finally I feel you now
(Ooh) On this never-ending road
(Ooh) Holding you so tight inside my dreams

It's like you've already filled me
I feel it again
So clear, your pure emotions
All the scenes I always create
Every time it's filled with you
Now I'm here
Blendin' feelings for you

Every cell inside me is reaching out to you
Even though we're a little apart, we're together
Yeah, maybe you don't but I love you
Nothing even matters because I'm in love

So now I'm
Trying to move on without you just like it is the end
Counting every day
Waiting day and night for a reason
Tell me, "Oh, bon voyage
Under the sky, oh, bon voyage"
Without any words, I still know
I know you, I know you

(Ooh) Someday in the season when flowers bloom
We were walking on the opposite sides, yeah (Ooh)
(Ooh) Is it twisted fates or fate's twisted game?
Seeing you in my dreams, a contradiction? Yeah (Ooh)
Call me crazy, didn't mean to hurt your heart
'Cause closer, sometimes drift apart
I know I'm selfish, can't deny, but I still see a future bright
The doubts and fears sometimes, they cloud in my mind
I can't help but hold on tight and never leave you behind

Every cell inside me is reaching out to you
Even though we're a little apart, we're together
Yeah, maybe you don't but I love you
Nothing even matters because I'm in love

So now I'm
Trying to move on without you just like it is the end
Counting every day
Waiting day and night for a reason
Tell me, "Oh, bon voyage
Under the sky, oh, bon voyage"
Without any words, I still know
I know you, I know you

I will call out to you just until the bitter end
So that you can hear me everywhere you may be, whoa

Bon voyage (Wa-a-a-a-ah)
Bon voyage
I want you to embrace
When our tomorrow
Comes knocking at the door
Bon voyage
Bon voyage
Now I really know you always
I know you, I know you""")

    def test_bad_song(self):
        """
        Testing a song that does not exist and asserting it fails gracefully.
        P.S. the correct song if 2 months, if you care to listen.
        :return: pass if fails as expected.
        """
        import analysis.lyric_grabber as lyric
        result = lyric.get_lyrics_tester(artist="uau", song="3 months")
        assert(result == "Sorry, I was unable to find that song.")

if __name__ == '__main__':
    unittest.main()
