import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.wpewebkit import options

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
link = driver.find_element(By.LINK_TEXT, "Incarca fisier")
link.click()
time.sleep(2)
file_input = driver.find_element(By.NAME, "file")
file_input.send_keys(r"C:\Users\Localadmin\Downloads\Test documente incarcate.pdf")
time.sleep(2)
dropdown = Select(driver.find_element(By.ID, "tip"))
dropdown.select_by_value("diploma_emc")
time.sleep(2)
dropdown = Select(driver.find_element(By.ID, "emc"))
dropdown.select_by_value("24")
time.sleep(2)
date_input = driver.find_element(By.NAME, "data")
date_input.send_keys("08/13/2025")  # Format MM/DD/YYYY
time.sleep(2)
submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Incarca']")
submit_button.click()
time.sleep(2)
if driver.current_url == 'https://probaamg.rdsweb.ro/user/3' and driver.find_element(By.XPATH, "//div[@class='alert alert-success']"):
    print("Incarcare reusita")
elif driver.current_url == 'https://probaamg.rdsweb.ro/user/3' and driver.find_element(By.XPATH, "//div[@class='alert alert-danger']"):
    print("Incarcare esuata")
time.sleep(2)
driver.close()

