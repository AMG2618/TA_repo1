from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('utilizatorul este autentificat și accesează pagina "Documente puncte EMC"')
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

    context.driver.find_element(By.XPATH, "//a[contains(text(), 'Documente puncte EMC')]").click()
    time.sleep(2)

@when('utilizatorul are mai puțin de 48 puncte EMC')
def step_impl(context):
    emc_text = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Total EMC:')]").text
    context.puncte_emc = int(emc_text.split(":")[1].strip())
    time.sleep(1)

@when('utilizatorul apasă pe butonul "Cerere viză"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/trimitecerereviza/3')]").click()
    time.sleep(2)

@then('sistemul afișează mesajul de eroare pentru puncte EMC insuficiente')
def step_impl(context):
    if context.puncte_emc < 48:
        mesaj = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Nu aveti suficiente puncte EMC')]").text
        assert "Nu aveti suficiente puncte EMC" in mesaj
        print("❌ Mesajul de eroare este afișat corect:", mesaj)
    else:
        print("⚠️ Utilizatorul are suficiente puncte EMC — nu se afișează mesaj de eroare.")
    context.driver.quit()
