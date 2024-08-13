from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=/home/halim/.config/google-chrome")
options.add_argument(r'--profile-directory=Halim Ibrahim')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://web.whatsapp.com")

driver.minimize_window()

import time

time.sleep(10)

finder = driver.find_element("xpath", "//div[contains(@class, 'x1y332i5 x1n2onr6 x6ikm8r x10wlt62')]")

f = open('numbers.txt', 'w')

print(finder)


driver.close()