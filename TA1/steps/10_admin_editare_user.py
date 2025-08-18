from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

@given('adminul este autentificat și accesează pagina "Lista utilizatori"')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://probaamg.rdsweb.ro/admin")
    time.sleep(2)

    context.driver.find_element(By.NAME, "username").send_keys("admin")
    time.sleep(1)
    context.driver.find_element(By.NAME, "password").send_keys("admin")
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Conectare']").click()
    time.sleep(2)

    context.driver.find_element(By.LINK_TEXT, "Lista utilizatori").click()
    time.sleep(2)

@when('adminul accesează formularul de editare pentru utilizatorul cu ID 3')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/admin/user/3/edit')]").click()
    time.sleep(2)

@when('modifică datele utilizatorului cu informații noi')
def step_impl(context):
    context.driver.find_element(By.NAME, "user").clear()
    context.driver.find_element(By.NAME, "user").send_keys("Anita25")
    time.sleep(1)

    context.driver.find_element(By.NAME, "parola").clear()
    context.driver.find_element(By.NAME, "parola").send_keys("Alimentare26#")
    time.sleep(1)

    context.driver.find_element(By.NAME, "nume").clear()
    context.driver.find_element(By.NAME, "nume").send_keys("Anita")

    context.driver.find_element(By.NAME, "prenume").clear()
    context.driver.find_element(By.NAME, "prenume").send_keys("Manescu")
    time.sleep(1)

    select = Select(context.driver.find_element(By.ID, "colegiu"))
    select.select_by_value("Bucuresti")
    time.sleep(1)

@when('adminul validează modificările')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(2)

@then('modificările ar trebui să fie salvate cu succes')
def step_impl(context):
    if context.driver.current_url == 'https://probaamg.rdsweb.ro/user/3':
        print("✅ Modificările efectuate cu succes.")
    else:
        print("❌ Modificările nu au fost salvate.")
    context.driver.quit()
