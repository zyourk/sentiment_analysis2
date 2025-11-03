import unittest


class MyTestCase(unittest.TestCase):

    def test_translate(self):
        # Would you believe me if I told you I was translating another Dreamcatcher song
        from analysis.translator import translate
        translated = translate("""
        (Ooh-ooh-ooh-ooh)
        (Ooh-ooh-ooh-ooh, ooh-ooh)
        (Ooh-ooh-ooh-ooh)
        (Ooh-ooh-ooh-ooh, ooh-ooh)
        
        또렷이 보여 새로운 wonder
        간절히 원한다면 그곳으로
        사랑을 느껴 걱정은 없어
        저 바다의 바람과
        설렘을 가득히 runnin' up
        
        Wonderful, wonderful sunrise
        Beautiful, beautiful moonlight
        파도에 반짝이는 빛을 가득 담아
        Hold on to me as we go fly
        더 높이 올라 나를 꽉 붙잡아 and now
        We're headin' for a surprise
        
        나 지금 빛나고 있는
        당신의 눈을 보면서
        동화 같은 꿈을 꿔
        빛 속에 젖어 춤추는
        신비한 너의 손잡아
        We're living a fairytale
        
        Follow your heart
        Follow your heart
        Follow your heart
        We're living in a fairytale
        
        Yeah, yeah 내게만 보여줘
        너의 뒤에 빛나는 날개를
        꿈인 줄 알았던 너와의 춤
        둘만의 속삭임
        왠지 턱 끝까지 차오르는 건
        약속된 이별 때문일까
        모든 순간을 남기고 싶어 이 설레임 까지 yeah
        
        Wonderful, wonderful sunrise
        Beautiful, beautiful moonlight
        순간의 마법 같은 바람을 느껴봐
        Hold on to me as we go fly
        두 팔을 벌려 나를 꽉 안고서 And now
        We're heading for a surprise
        
        나 지금 빛나고 있는
        당신의 눈을 보면서
        동화 같은 꿈을 꿔
        빛 속에 젖어 춤추는
        신비한 너의 손잡아
        We're living a fairytale
        (Ooh-ooh-ooh-ooh)
        (Ooh-ooh-ooh-ooh, ooh-ooh)
        We're living in a fairytale
        (Ooh-ooh-ooh-ooh) Whoa-oh-oh
        (Ooh-ooh-ooh-ooh, ooh-ooh)
        
        I see a dream inside my eyes
        You are the dream inside my eyes
        I'm living a fairytale
        This might sound like a fantasy
        Don't worry, look up and you'll see
        You're living a fairytale
        
        Ooh-ooh-ooh (Ooh-ooh-ooh-ooh)
        Ooh-ooh-ooh-ooh (Ooh-ooh-ooh-ooh, ooh-ooh)
        Ooh-ooh-ooh (Ooh-ooh-ooh-ooh)
        Ooh-ooh-ooh-ooh (Ooh-ooh-ooh-ooh, ooh-ooh)
        Follow your heart (Ooh-ooh-ooh-ooh)
        Follow your heart (Ooh-ooh-ooh-ooh, ooh-ooh)
        Follow your heart (Ooh-ooh-ooh-ooh)
        We're living in a fairytale (Ooh-ooh-ooh-ooh, ooh-ooh)""")
        print(translated)

    def test_translate_more(self):
        # Crazy news I'm translating a song from my other favorite band
        from analysis.translator import translate
        translated = translate("""
        雨が降った　花が散った
        ただ染まった　頬を想った
        僕はずっと　バケツいっぱいの月光を飲んでる
        
        本当なんだ　夜みたいで
        薄く透明な口触りで
        そうなんだって
        笑ってもいいけど
        僕は君を待っている
        
        夏が去った　街は静か
        僕はやっと　部屋に戻って
        夜になった　こんな宵月を一人で見ている
        本当なんだ　昔の僕は
        涙が宝石でできてたんだ
        そうなんだって　笑ってもいいけど
        声はもう特に忘れた
        思い出も愛も死んだ
        風のない海辺を歩いた　あの夏へ
        
        僕はさよならが欲しいんだ
        ただ微睡むような
        もの一つさえ言わないまま
        僕は君を待っている
        
        歳を取った　一つ取った
        何も無い部屋で　春になった
        僕は愛を底が抜けた　柄酌で飲んでる
        本当なんだ　味もしなくて
        飲めば飲むほど喉が渇いて
        そうなんだって　笑ってもいいけど
        
        僕は夜を待っている
        君の鼻歌が欲しいんだ
        ただ微睡むような
        もの一つさえ言わないまま
        
        僕は君を待っている
        君の目を覚えていない
        君の口を描いていない
        もの一つさえ言わないまま
        
        僕は君を待っていない
        君の鼻を知っていない
        君の頬を思っていない
        さよならすら言わないまま
        
        君は夜になって行く
        
        (本当なんだ　夜みたいで
        夏が透明な口触りで)""")
        print(translated)

    def test_english_check(self):
        from analysis.translator import check_english
        english = check_english("""
        Talk to me
        Come on, baby, won't you let me see?
        All the shit you've done to f—
        
        Throw a flare, we gon' meet back here
        I've been told that love is war, I don't need no tears
        Good to go, I'm strapped in
        Call into control, ready for extraction
        You know there ain't no respawn (Check, check, check, check)
        Gun got a sensor, I can see him as a heat dot (Check, check, check, check)
        Give me a signal, then he'll go missing (Check, check, check, check)
        You're all that remains, finish the mission (Check, check)
        
        I'm with my soldier, we deploy (Soldier, we deploy)
        You're the last one left, search and destroy
        Hope the suppressor kill the noise (Ah, ah)
        I drown my cup to fill the void
        I'm with my soldier, we deploy (Soldier, we deploy)
        You're the last one left, search and destroy
        Hope the suppressor kill the noise (Ah, ah)
        I drown my cup to fill the void
        
        It's a free-for-all
        You wanna feast with the team, it ain't cheap at all
        (Feast, f-f— Uh, ah)
        I'm pulling on the rope, get the rest, it's time to go
        I know a place where we can hide, a couple clicks right down the road
        I gave them my soul, but they still treat me like a boy
        My father always told me that a gun is not a toy
        Got a little quiet, they're the ones we should avoid
        
        I'm with my soldier, we deploy (Soldier, we deploy)
        You're the last one left, search and destroy
        Hope the suppressor kill the noise (Ah, ah)
        I drown my cup to fill the void
        I'm with my soldier, we deploy (Check, check, check, check)
        You're the last one left, search and destroy (Check, check, check, check)
        Hope the suppressor kill the noise (Check, check, check, check)
        I drown my cup to fill the void (Check, check, check, check)
        
        Talk to me
        Come on, baby, won't you let me see?
        All the shit you've done to f—""")
        assert english

    def test_check_not_english(self):
        from analysis.translator import check_english
        english = check_english("""
        (Ooh-ooh-ooh-ooh)
        (Ooh-ooh-ooh-ooh, ooh-ooh)
        (Ooh-ooh-ooh-ooh)
        (Ooh-ooh-ooh-ooh, ooh-ooh)
        
        또렷이 보여 새로운 wonder
        간절히 원한다면 그곳으로
        사랑을 느껴 걱정은 없어
        저 바다의 바람과
        설렘을 가득히 runnin' up
        
        Wonderful, wonderful sunrise
        Beautiful, beautiful moonlight
        파도에 반짝이는 빛을 가득 담아
        Hold on to me as we go fly
        더 높이 올라 나를 꽉 붙잡아 and now
        We're headin' for a surprise
        
        나 지금 빛나고 있는
        당신의 눈을 보면서
        동화 같은 꿈을 꿔
        빛 속에 젖어 춤추는
        신비한 너의 손잡아
        We're living a fairytale
        
        Follow your heart
        Follow your heart
        Follow your heart
        We're living in a fairytale
        
        Yeah, yeah 내게만 보여줘
        너의 뒤에 빛나는 날개를
        꿈인 줄 알았던 너와의 춤
        둘만의 속삭임
        왠지 턱 끝까지 차오르는 건
        약속된 이별 때문일까
        모든 순간을 남기고 싶어 이 설레임 까지 yeah
        
        Wonderful, wonderful sunrise
        Beautiful, beautiful moonlight
        순간의 마법 같은 바람을 느껴봐
        Hold on to me as we go fly
        두 팔을 벌려 나를 꽉 안고서 And now
        We're heading for a surprise
        
        나 지금 빛나고 있는
        당신의 눈을 보면서
        동화 같은 꿈을 꿔
        빛 속에 젖어 춤추는
        신비한 너의 손잡아
        We're living a fairytale
        (Ooh-ooh-ooh-ooh)
        (Ooh-ooh-ooh-ooh, ooh-ooh)
        We're living in a fairytale
        (Ooh-ooh-ooh-ooh) Whoa-oh-oh
        (Ooh-ooh-ooh-ooh, ooh-ooh)
        
        I see a dream inside my eyes
        You are the dream inside my eyes
        I'm living a fairytale
        This might sound like a fantasy
        Don't worry, look up and you'll see
        You're living a fairytale
        
        Ooh-ooh-ooh (Ooh-ooh-ooh-ooh)
        Ooh-ooh-ooh-ooh (Ooh-ooh-ooh-ooh, ooh-ooh)
        Ooh-ooh-ooh (Ooh-ooh-ooh-ooh)
        Ooh-ooh-ooh-ooh (Ooh-ooh-ooh-ooh, ooh-ooh)
        Follow your heart (Ooh-ooh-ooh-ooh)
        Follow your heart (Ooh-ooh-ooh-ooh, ooh-ooh)
        Follow your heart (Ooh-ooh-ooh-ooh)
        We're living in a fairytale (Ooh-ooh-ooh-ooh, ooh-ooh)""")
        assert not english

    def test_romanji(self):
        from analysis.translator import translate
        result = translate("""
        Kangaetatte wakaranaishi
        Aozora no shita kimi o matta
        Kaze ga fuita shougo
        Hirusagari o nukedasu souzou
        Nee, kore kara dou narun darou ne
        Susume kata osowaranainda yo
        Kimi no me o mita
        Nanimo iezu boku wa aruita
        
        
        Kangaetatte wakaranaishi
        Seishun nante tsumaranaishi
        Yameta hazu no piano, tsuukue o hiku kuse ga nukenai
        Nee, shourai nani shiteru darou ne
        Ongaku wa shite naito ii ne
        Komaranaide yo
        
        Kokoro no naka ni hitotsu sen o hiite mo
        Doushite mo kienakatta ima sara nanda kara
        Naa, mou omoidasu na
        
        Machigatterun da yo
        Wakattenai yo
        Antara ningen mo
        Hontou mo ai mo sekai mo
        Kurushisa mo jinsei mo
        Dou demo ii yo
        Tadashii ka dou ka shiritai no datte bouei honnou da
        Kangaetanda, anta no sei da
        
        Kangaetatte wakaranai ga
        Hontou ni toshi oitakunainda
        Itsuka shindaratte
        Omou dake de mune ga karappo ni narunda
        Shourai nanishiteru darou tte
        Otona ni nattara wakatta yo
        Nanmo shitenai sa
        
        Shiawase na kao
        Shita hito ga nikui no wa
        Dou warikittara ii nda
        Mitasarenai atama no oku no
        Bakemono mitai na rettoukan
        
        Machigattenai yo na
        Nanda ka nda antara ningen da
        Ai mo sukui mo yasashisa mo
        Konkyo ga nai nante
        Kimi ga warui yo
        Rabusongu nanka ga itai
        No datte boei honnou da
        Dou demo ii ka
        Anta no sei da
        
        Kangaetatte wakaranaishi
        Ikiteru dake demo kurushiishi
        Ongaku to ka mou karanaishi
        Kashito ka tekitou demo ii yo
        Dou demo ii nda
        Machigattenai darou
        Machigattenai yo na
        Machigattenai yo na
        
        Machigatterunda yo
        Wakatterunda antara ningen mo
        Hontou mo ai mo sukui mo
        Yasashisa mo jinsei mo
        Dou demo iin da
        Tadashii kotae ga ienai
        No datte boei honnou da
        Dou demo ii ya
        Anta no seida
        
        (Aaah) Boku datte shinnen ga atta
        Ima ja gomi mitai na omoi da
        Nando demo kimi o kaita
        Ureru koto koso ga dou demo yokatta nda
        Hontou da hontou na nda
        Mukashi wa sou datta
        Dakara boku wa
        Dakara boku wa
        Ongaku o yameta""")
        print(result)


if __name__ == '__main__':
    unittest.main()
