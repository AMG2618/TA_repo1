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

@when('utilizatorul accesează linkul către lista documentelor încărcate')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@href='/fisier/3']").click()
    time.sleep(2)

@then('pagina cu lista documentelor încărcate ar trebui să fie afișată')
def step_impl(context):
    if context.driver.current_url == 'https://probaamg.rdsweb.ro/fisier/3':
        print("✅ Lista documentelor încărcate este vizibilă.")
    else:
        print("❌ Eroare la accesarea listei documentelor încărcate.")
    context.driver.close()
