import googletrans as gt

transl = gt.Translator()

def ara_en(txt):
    return transl.detect(txt)

def en_ara(txt):
    return transl.translate(txt, dest='ar')

print(ara_en('أنا أحب المانجو في الصيف'))

#not working figure it out later