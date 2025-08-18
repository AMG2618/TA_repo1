import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://probaamg.rdsweb.ro/login")
driver.maximize_window()
# Introducere date pentru inregistrare
username_input = driver.find_element(By.NAME, "username").send_keys("proba12")
time.sleep(2)
password_input = driver.find_element(By.NAME, "password").send_keys("Alimentare25#")
time.sleep(2)
# acceseaza pagina de documente
submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Conectare']")
submit_button.click()
time.sleep(2)
link = driver.find_element(By.XPATH, "//a[@href='/fisier/6']")
link.click()

time.sleep(2)
# Setează directorul de descărcare
if not os.path.exists(r"C:\Users\Localadmin\Downloads"):
    os.makedirs(r"C:\Users\Localadmin\Downloads")
import os
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\Localadmin\Downloads",  # Directorul unde se vor descărca fișierele
    "download.prompt_for_download": False,  # Nu cere confirmarea pentru descărcare
    "download.directory_upgrade": True,  # Permite actualizarea directorului de descărcare
    "safebrowsing.enabled": True  # Activează navigarea sigură
})
driver = webdriver.Chrome(options=chrome_options)
import time
from selenium.webdriver.common.by import By
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# Setează opțiunile pentru Chrome
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\Localadmin\Downloads",  # Directorul unde se vor descărca fișierele
    "download.prompt_for_download": False,  # Nu cere confirmarea pentru descărcare
    "download.directory_upgrade": True,  # Permite actualizarea directorului de descărcare
    "safebrowsing.enabled": True  # Activează navigarea sigură
})
# Găsește toate linkurile „Descarcă fișier”
links = driver.find_elements(By.LINK_TEXT, "Descarcă fișier")

# Click pe fiecare pentru descărcare
for link in links:
    link.click()
    time.sleep(2)  # Așteapta descarcarea
driver.close()
