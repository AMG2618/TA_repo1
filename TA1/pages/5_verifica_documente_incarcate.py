import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://probaamg.rdsweb.ro/login")
time.sleep(2)

username_input = driver.find_element(By.NAME, "username").send_keys("Anita25")
time.sleep(2)
password_input = driver.find_element(By.NAME, "password").send_keys("Alimentare26#")
time.sleep(2)
submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Conectare']")
submit_button.click()
time.sleep(2)
link = driver.find_element(By.XPATH, "//a[@href='/fisier/3']")
link.click()
if driver.current_url == 'https://probaamg.rdsweb.ro/fisier/3':
    print("Lista documentelor incarcate este vizibila")
else:
    print("Eroare la accesarea listei documentelor incarcate")
time.sleep(2)
driver.close()