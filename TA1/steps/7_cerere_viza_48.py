from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('utilizatorul este autentificat în aplicație')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://probaamg.rdsweb.ro/login")
    time.sleep(2)

    context.driver.find_element(By.NAME, "username").send_keys("Anita25")
    time.sleep(1)
    context.driver.find_element(By.NAME, "password").send_keys("Alimentare26#")
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Conectare']").click()
    time.sleep(2)

@when('utilizatorul accesează secțiunea "Documente puncte EMC"')
def step_impl(context):
    link_docEMC = context.driver.find_element(By.XPATH, "//a[contains(@href, '/viza/3')]")
    link_docEMC.click()
    time.sleep(2)

@when('verifică numărul de puncte EMC')
def step_impl(context):
    emc_text = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Total EMC: 48')]").text
    context.puncte_emc = int(emc_text.split(":")[1].strip())
    time.sleep(1)

@when('utilizatorul apasă pe butonul "Cerere viză"')
def step_impl(context):
    btn_cerere = context.driver.find_element(By.XPATH, "//a[contains(@href, '/trimitecerereviza/3')]")
    btn_cerere.click()
    time.sleep(2)

@then('cererea de viză este trimisă doar dacă punctele EMC sunt suficiente')
def step_impl(context):
    if context.puncte_emc >= 48:
        print("✅ A fost trimisa cu succes cererea de viză.")
    else:
        print("❌ Eroare: puncte EMC insuficiente pentru trimiterea cererii.")
    context.driver.quit()