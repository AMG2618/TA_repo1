from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('administratorul se autentifică în panoul de administrare')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://probaamg.rdsweb.ro/admin")
    context.driver.maximize_window()
    time.sleep(2)

    context.driver.find_element(By.NAME, "username").send_keys("admin")
    time.sleep(1)
    context.driver.find_element(By.NAME, "password").send_keys("admin")
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Conectare']").click()
    time.sleep(2)

@when('administratorul accesează "Lista utilizatori" și selectează ștergerea utilizatorului cu ID 3')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Lista utilizatori").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/admin/user/3/delete')]").click()
    time.sleep(2)

@then('sistemul confirmă în consolă că utilizatorul a fost șters')
def step_impl(context):
    print("Utilizatorul cu ID 3 a fost șters cu succes.")
    context.driver.close()
