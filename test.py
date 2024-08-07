from deep_translator import GoogleTranslator

translated = GoogleTranslator(source='auto', target='en').translate('أنا أحب العالم')
translated_1 = GoogleTranslator(source='auto', target='ar').translate('I love the world')
print(translated_1)