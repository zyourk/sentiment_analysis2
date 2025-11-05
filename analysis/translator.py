from googletrans import Translator

"""
This file houses the functionality for translating lyrics
It was... much smaller than I had expected it to be
"""


"""
Translates text into English by default
"""
def translate(text):
    from googletrans import Translator
    translator = Translator()
    return translator.translate(text).text
"""
Checks if text is in English
If not, it will be translated
"""
def check_english(text):
    # from googletrans import Translator
    # translator = Translator()
    # return translator.detect(text).lang == "en"
    import langid
    lang = langid.classify(text)[0]
    return lang == "en"