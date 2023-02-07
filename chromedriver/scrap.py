from selenium import webdriver
import time
from fake_useragent import UserAgent
import random
from selenium.webdriver.common.by import By


useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0')
driver = webdriver.Chrome(
    executable_path='C:\\my_project\\kaspi_pars\\chromedriver\\chromedriver.exe',
    options=options)
url = 'https://kaspi.kz/shop/p/kelet-evn-k-4-5-e3-220-8500438/?c=151010000'


try:
    driver.get(url=url)
    time.sleep(2)
    city_choice = driver.find_element(By.CLASS_NAME, 'current-location__dialog-lists')
    city = city_choice.find_element(By.LINK_TEXT, 'Актобе').click()
    price = driver.find_element(By.CLASS_NAME, 'item__price-once').text
    print(price)
    
    time.sleep(5)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
