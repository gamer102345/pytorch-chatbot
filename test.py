from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://web.whatsapp.com")

driver.minimize_window()
while True:
    try:
        finder = driver.find_element("xpath", "//div[contains(@class, '_aou8 _aj_h')]")
        break
    except:
        pass

for x in finder:
    if 'Momma' in x.get_attribute('InnerHTML'):
        x.click()

driver.close()