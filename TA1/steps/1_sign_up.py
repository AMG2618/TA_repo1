from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

@given('utilizatorul accesează pagina de înregistrare')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://probaamg.rdsweb.ro/inregistrare")
    time.sleep(2)

@when('completează câmpul "user" cu "proba12"')
def step_impl(context):
    context.driver.find_element(By.NAME, "user").send_keys("proba12")
    time.sleep(1)

@when('completează câmpul "parola" cu "Alimentare25#"')
def step_impl(context):
    context.driver.find_element(By.NAME, "parola").send_keys("Alimentare25#")
    time.sleep(1)

@when('completează câmpul "nume" cu "Anita"')
def step_impl(context):
    context.driver.find_element(By.NAME, "nume").send_keys("Anita")
    time.sleep(1)

@when('completează câmpul "prenume" cu "Popiescu"')
def step_impl(context):
    context.driver.find_element(By.NAME, "prenume").send_keys("Popiescu")
    time.sleep(1)

@when('selectează "Brasov" din dropdown-ul "colegiu"')
def step_impl(context):
    dropdown = Select(context.driver.find_element(By.ID, "colegiu"))
    dropdown.select_by_value("Brasov")
    time.sleep(1)

@when('apasă pe butonul "Inregistrare"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Inregistrare']").click()
    time.sleep(2)

@then('ar trebui să fie redirecționat către pagina de login')
def step_impl(context):
    assert context.driver.current_url == 'https://probaamg.rdsweb.ro/login'

@then('mesajul "Inregistrare reusita" este afișat în consolă')
def step_impl(context):
    print("Inregistrare reusita")
    context.driver.quit()
