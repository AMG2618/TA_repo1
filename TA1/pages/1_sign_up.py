import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://probaamg.rdsweb.ro/inregistrare")
driver.maximize_window()
# Introducere date pentru inregistrare
username_input = driver.find_element(By.NAME, "user").send_keys("proba12")
time.sleep(2)
password_input = driver.find_element(By.NAME, "parola").send_keys("Alimentare25#")
time.sleep(2)
driver.find_element(By.NAME, "nume").send_keys("Anita")
time.sleep(2)
driver.find_element(By.NAME, "prenume").send_keys("Popiescu")
time.sleep(2)
dropdown = Select(driver.find_element(By.ID, "colegiu"))
dropdown.select_by_value("Brasov")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@type='submit' and @value='Inregistrare']").click()
time.sleep(2)
if driver.current_url == 'https://probaamg.rdsweb.ro/login':
    print("Inregistrare reusita")
else:
    print("Inregistrare esuata")
time.sleep(2)
driver.close()
