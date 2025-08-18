import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://probaamg.rdsweb.ro/login")
time.sleep(2)

username_input = driver.find_element(By.NAME, "username").send_keys("proba12")
time.sleep(2)

username_input = driver.find_element(By.NAME, "password").send_keys("Alimentare25#")
time.sleep(2)

submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Conectare']")
submit_button.click()
time.sleep(2)
if driver.current_url == 'https://probaamg.rdsweb.ro/user/6':
    print("Conectare reusita")
else:
    print("Conectare esuata")
time.sleep(2)
driver.close()


