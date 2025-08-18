import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://probaamg.rdsweb.ro/admin")
driver.maximize_window()
# Introducere date pentru logare ca admin
username_input = driver.find_element(By.NAME, "username").send_keys("admin")
time.sleep(2)
password_input = driver.find_element(By.NAME, "password").send_keys("admin")
time.sleep(2)
submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Conectare']")
submit_button.click()
time.sleep(2)
# Gasește linkul după text
link_lista = driver.find_element(By.LINK_TEXT, "Lista utilizatori")
link_lista.click()
time.sleep(2)
# editare utilizator
link_editeaza = driver.find_element(By.XPATH, "//a[contains(@href, '/admin/user/3/edit')]")
link_editeaza.click()
# driver.find_element(By.LINK_TEXT, "Editeaza user").click()
time.sleep(2)
# Completează câmpurile
driver.find_element(By.NAME, "user").clear()
driver.find_element(By.NAME, "user").send_keys("Anita25")
time.sleep(2)

driver.find_element(By.NAME, "parola").clear()
driver.find_element(By.NAME, "parola").send_keys("Alimentare26#")
time.sleep(2)

driver.find_element(By.NAME, "nume").clear()
driver.find_element(By.NAME, "nume").send_keys("Anita")

driver.find_element(By.NAME, "prenume").clear()
driver.find_element(By.NAME, "prenume").send_keys("Manescu")
time.sleep(2)

# Selectează colegiul
select = Select(driver.find_element(By.ID, "colegiu"))
select.select_by_value("Bucuresti")

# valideaza modificările
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)

# Verifică dacă modificările au fost salvate
if driver.current_url == 'https://probaamg.rdsweb.ro/user/3':
    print("Modificări efectuate cu succes")
else:
    print("Modificări eșuate")
time.sleep(2)
# Inchide browserul
driver.quit()