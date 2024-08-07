import googletrans as gt

transl = gt.Translator()

def ara_en(src):
    return transl.translate(text=src, dest='en', src='auto')

def en_ara(src):
    return transl.translate(text=src, dest='ar', src='auto')

print(en_ara('I love mangos in the summer'))