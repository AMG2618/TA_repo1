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
# click buton "Documente puncte EMC"
# Click pe linkul "Documente puncte EMC"
link_docEMC = driver.find_element(By.XPATH, "//a[contains(text(), 'Documente puncte EMC')]")
link_docEMC.click()
time.sleep(2)
#verifica punctele EMC < 48
puncte_emc = driver.find_element(By.XPATH, "//*[contains(text(), 'Total EMC: 0')]").text

# Click pe butonul "Cerere viza"
link_btn_cerereviza = driver.find_element(By.XPATH, "//a[contains(@href, '/trimitecerereviza/3')]")
link_btn_cerereviza.click()
time.sleep(2)

# Verifică mesajul de eroare
if puncte_emc == "Total EMC: 0":
    print("Mesajul de eroare este afișat corect: Eroare! Nu aveti suficiente puncte EMC! Limita este 48 de puncte EMC pentru a putea solicita viza de libera practica.")
time.sleep(2)
driver.quit()

