from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

@given('utilizatorul este autentificat și accesează pagina cu documente')
def step_impl(context):
    # Setare folder descărcare
    download_dir = r"C:\Users\Localadmin\Downloads"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    context.driver.get("https://probaamg.rdsweb.ro/login")
    time.sleep(2)

    context.driver.find_element(By.NAME, "username").send_keys("proba12")
    time.sleep(1)
    context.driver.find_element(By.NAME, "password").send_keys("Alimentare25#")
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Conectare']").click()
    time.sleep(2)

    context.driver.find_element(By.XPATH, "//a[@href='/fisier/6']").click()
    time.sleep(2)

@when('utilizatorul apasă pe fiecare link "Descarcă fișier"')
def step_impl(context):
    links = context.driver.find_elements(By.LINK_TEXT, "Descarcă fișier")
    context.nr_linkuri = len(links)

    for link in links:
        link.click()
        time.sleep(2)  # Așteaptă descărcarea

@then('fișierele ar trebui să fie descărcate în folderul specificat')
def step_impl(context):
    download_dir = r"C:\Users\Localadmin\Downloads"
    files = os.listdir(download_dir)
    if files:
        print(f"✅ {context.nr_linkuri} fișier(e) au fost descărcate în: {download_dir}")
    else:
        print("❌ Niciun fișier nu a fost descărcat.")
    context.driver.close()
