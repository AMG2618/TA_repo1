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
# acceseaza cereri EMC
link_cereri_viza = driver.find_element(By.XPATH, "//a[contains(@href, '/admin/cereri_viza')]")
link_cereri_viza.click()
time.sleep(2)
# Verifică dacă a fost redirecționat către pagina cererilor de viză EMC
if "/admin/cereri_viza" in driver.current_url:
    print("Adminul a accesat cu succes pagina cererilor de viză EMC.")