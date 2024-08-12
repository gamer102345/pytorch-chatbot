exeption_numbers = ['+97338301209', '+97366762845', '+966541444824', '+97366762840', '+97333284961',
                    '+966551309290', '+97333243838'] #to add to


from deep_translator import GoogleTranslator

from train import tren
from chat import chitter

tren()

#change this to use arabic if needed
chitter()

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

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

