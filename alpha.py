from deep_translator import GoogleTranslator


def ara_en(src):
    return GoogleTranslator(source='auto', target='en').translate(src)

def en_ara(src):
    return GoogleTranslator(source='auto', target='ar').translate(src)

inp = 'x' #placeholder
english_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if english_alpha in inp:
    #return ai stuff in english
    pass
else:
    ara_en(inp)
    #do the ai stuff then return in arabic

#whatsapp api

def texting(text):
    import pywhatkit
