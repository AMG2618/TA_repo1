from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('adminul accesează pagina de login pentru administrare')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://probaamg.rdsweb.ro/admin")
    time.sleep(2)

@when('completează câmpul "username" cu "admin" și "password" cu "admin"')
def step_impl(context):
    context.driver.find_element(By.NAME, "username").send_keys("admin")
    time.sleep(1)
    context.driver.find_element(By.NAME, "password").send_keys("admin")
    time.sleep(1)

@when('apasă pe butonul "Conectare"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Conectare']").click()
    time.sleep(2)

@when('adminul accesează secțiunea "Cereri viză EMC"')
def step_impl(context):
    link_cereri_viza = context.driver.find_element(By.XPATH, "//a[contains(@href, '/admin/cereri_viza')]")
    link_cereri_viza.click()
    time.sleep(2)

@then('ar trebui să fie redirecționat către pagina cu cererile de viză EMC')
def step_impl(context):
    assert "/admin/cereri_viza" in context.driver.current_url
    print("✅ Adminul a accesat cu succes pagina cererilor de viză EMC.")
    context.driver.quit()
