import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://probaamg.rdsweb.ro/login")
time.sleep(2)

username_input = driver.find_element(By.NAME, "username").send_keys("Anita25")
time.sleep(2)

username_input = driver.find_element(By.NAME, "password").send_keys("Alimentare26#")
time.sleep(2)

submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Conectare']")
submit_button.click()
# Click pe linkul "Documente puncte EMC"
link_docEMC = driver.find_element(By.XPATH, "//a[contains(@href, '/viza/3')]")
link_docEMC.click()
time.sleep(2)
#verifica punctele EMC = 48
puncte_emc = driver.find_element(By.XPATH, "//*[contains(text(), 'Total EMC: 48')]").text
time.sleep(2)
# Click pe butonul "Cerere viza"
link_btn_cerereviza = driver.find_element(By.XPATH, "//a[contains(@href, '/trimitecerereviza/3')]")
link_btn_cerereviza.click()
time.sleep(2)

# Verifică mesajul de eroare
if puncte_emc == "Total EMC: 48":
    print("A fost trimisa cu succes cererea de viză.")
else:
    print("Eroare trimitere cerere.")
time.sleep(2)
driver.quit()

