exeption_numbers = ['+97338301209', '+97366762845', '+966541444824', '+97366762840', '+97333284961',
                    '+966551309290', '+97333243838'] #to add to


import concurrent.futures.thread
from deep_translator import GoogleTranslator
import pywhatkit.whats

from train import tren
from chat import chitter

tren()

#change this to use arabic if needed

#this should be in a while loop

def ara_en(src):
    return GoogleTranslator(source='auto', target='en').translate(src)

def en_ara(src):
    return GoogleTranslator(source='auto', target='ar').translate(src)

english_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#whatsapp api

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://web.whatsapp.com")

driver.minimize_window()

finder = driver.find_element("xpath", "//div[contains(@class, '_aou8 _aj_h')]")

numbers = []

for f in finder:
    if f is int:
        numbers.append(f)

def read_and_write(number):
    #run script AI for each number

    ending = ["Ok, let me forward you to a higher up", "A representative of the company will be contacting you shortly", "Thank you for inquiring", "Glad to have answered your questions!"]

    #now read their texts
    while True:
        #should be a number in numbers [should be part of the threads of functions]
        finder_1 = driver.find_element("xpath", f"//div[contains(@class, 'x9f619 x1hx0egp x1yrsyyn x1ct7el4 x1dm7udd xwib8y2')][.//div[text()[contains(., '{number}')]][.//div[contains(@class, '_akbar')]]") 

        driver.close

        from pywhatkit import whats

        for text in finder_1:
            if english_alpha in text:
                #return ai stuff in english
                response = chitter(text) #should enter it into the ai
                if text in ending:
                    #change to walid's number
                    whats.sendwhatmsg_instantly('+97338301209', str(number))
                    return 1
                whats.sendwhatmsg_instantly(number, response) #TODO: change numbers
            else:
                arabic_to_eng = ara_en(text)
                response_0 = chitter(arabic_to_eng)
                reponse_1 = en_ara(response_0)
                if text in ending:
                    #change to walid's number
                    whats.sendwhatmsg_instantly('+97338301209', str(number))
                    return 1
                whats.sendwhatmsg_instantly(number, reponse_1)

import concurrent.futures   
pool = concurrent.futures.ThreadPoolExecutor(max_workers=len(numbers))

for x in numbers:
    pool.submit(read_and_write, x)  