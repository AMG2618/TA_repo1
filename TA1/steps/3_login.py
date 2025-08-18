from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('utilizatorul accesează pagina de login')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://probaamg.rdsweb.ro/login")
    time.sleep(2)

@when('introduce username "proba12" și parola "Alimentare25#"')
def step_impl(context):
    context.driver.find_element(By.NAME, "username").send_keys("proba12")
    time.sleep(1)
    context.driver.find_element(By.NAME, "password").send_keys("Alimentare25#")
    time.sleep(1)

@when('apasă pe butonul "Conectare"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Conectare']").click()
    time.sleep(2)

@then('utilizatorul ar trebui să fie redirecționat către pagina personală')
def step_impl(context):
    if context.driver.current_url == 'https://probaamg.rdsweb.ro/user/6':
        print("✅ Conectare reușită")
    else:
        print("❌ Conectare eșuată")
    time.sleep(1)
    context.driver.close()
