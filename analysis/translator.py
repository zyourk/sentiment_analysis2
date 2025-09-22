from googletrans import Translator

"""
This file houses the functionality for translating lyrics
It was... much smaller than I had expected it to be
"""

translator = Translator()

"""
Translates text into English by default
"""
def translate(text):
    return translator.translate(text).text

"""
Checks if text is in English
If not, it will be translated
"""
def check_english(text):
    return translator.translate(text).src == "en"