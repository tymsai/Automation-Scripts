import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    driver = webdriver.Chrome()
    driver.get('http://www.youtube.com')
    driver.maximize_window()
    time.sleep(1)
    search = driver.find_element(By.XPATH,'//input[@id="search"]')
    searchBTN = driver.find_element(By.XPATH,'//*[@id="search-icon-legacy"]')
    search.send_keys('python bot')
    time.sleep(5)
    searchBTN.send_keys(Keys.RETURN)
    time.sleep(5)
    print("Page title is:", driver.title)
except:
    print("error sai")
finally:
    driver.quit()
