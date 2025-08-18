from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

@given('Utilizatorul se autentifică și încarcă un fișier EMC valid')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://probaamg.rdsweb.ro/login")
    time.sleep(2)

    context.driver.find_element(By.NAME, "username").send_keys("proba12")
    time.sleep(1)
    context.driver.find_element(By.NAME, "password").send_keys("Alimentare25#")
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Conectare']").click()
    time.sleep(2)

    context.driver.find_element(By.LINK_TEXT, "Incarca fisier").click()
    time.sleep(2)

@when('utilizatorul completează formularul de încărcare cu fișierul și datele EMC')
def step_impl(context):
    context.driver.find_element(By.NAME, "file").send_keys(r"C:\Users\Localadmin\Downloads\Test documente incarcate.pdf")
    time.sleep(1)

    Select(context.driver.find_element(By.ID, "tip")).select_by_value("diploma_emc")
    time.sleep(1)

    Select(context.driver.find_element(By.ID, "emc")).select_by_value("24")
    time.sleep(1)

    context.driver.find_element(By.NAME, "data").send_keys("08/13/2025")  # MM/DD/YYYY
    time.sleep(1)

@when('utilizatorul apasă pe butonul "Incarca"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Incarca']").click()
    time.sleep(2)

@then('sistemul afișează mesajul de succes sau eroare corespunzător')
def step_impl(context):
    current_url = context.driver.current_url
    if current_url == 'https://probaamg.rdsweb.ro/user/3':
        try:
            success = context.driver.find_element(By.XPATH, "//div[@class='alert alert-success']")
            print("✅ Încărcare reușită:", success.text)
        except:
            error = context.driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")
            print("❌ Încărcare eșuată:", error.text)
    else:
        print("❌ Redirecționare greșită după încărcare.")
    context.driver.close()
