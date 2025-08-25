from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from features.pages.base_page import BasePage

#from browser import Browser

SIGN_UP_PAGE_URL = "https://probaamg.rdsweb.ro/inregistrare"

#class SignUpPage(Browser):
class SignUpPage(BasePage):

    INPUT_USER = (By.NAME, "user")
    INPUT_PASSWORD = (By.NAME, "parola")
    INPUT_NUME = (By.NAME, "nume")
    INPUT_PRENUME = (By.NAME, "prenume")
    INPUT_COLEGIU = (By.ID, "colegiu")
    BUTTON_SUBMIT = (By.XPATH, "//input[@type='submit' and @value='Inregistrare']")
    MESAJ_EROARE = (By.CLASS_NAME, "error")

    def open(self):
        self.driver.get(SIGN_UP_PAGE_URL)

    def fill_user(self, text_user):
        self.driver.find_element(By.NAME, "user").send_keys(text_user)

    def fill_password(self, text_pass):
        self.driver.find_element(By.NAME, "parola").send_keys(text_pass)

    def fill_nume(self, text_nume):
        self.driver.find_element(By.NAME, "nume").send_keys(text_nume)

    def fill_prenume(self, text_prenume):
        self.driver.find_element(By.NAME, "prenume").send_keys(text_prenume)

    def fill_colegiu(self, colegiu_value):
        dropdown = Select(self.driver.find_element(By.ID, "colegiu"))
        dropdown.select_by_value(colegiu_value)

    def click_inregistrare(self):
        #self.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Inregistrare']").click()
        self.click(self.BUTTON_SUBMIT)

    def verify_signup_url(self, expected_url):
        current_url = self.driver.current_url
        print(f"[DEBUG] Expected: {expected_url}")
        print(f"[DEBUG] Actual: {current_url}")
        return expected_url in current_url
