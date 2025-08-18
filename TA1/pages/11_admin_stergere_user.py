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
link_sterge = driver.find_element(By.XPATH, "//a[contains(@href, '/admin/user/3/delete')]")
link_sterge.click()
time.sleep(2)
# Afiseaza mesaj de confirmare stergere utilizator
print("Utilizatorul cu ID 3 a fost șters cu succes.")
driver.close()

