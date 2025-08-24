from selenium.webdriver.common.by import By
from browser import Browser

SIGN_UP_PAGE_URL = "https://probaamg.rdsweb.ro/inregistrare"

class SignUpPage(Browser):
    INPUT_USER = (By.NAME, "user")
    INPUT_PASSWORD = (By.NAME, "parola")
    INPUT_NUME = (By.NAME, "nume")
    INPUT_PRENUME = (By.NAME, "prenume")
    INPUT_COLEGIU = (By.NAME, "colegiu")
    BUTTON_SUBMIT = (By.XPATH, "//input[@type='submit' and @value='Inregistrare']")

    def open(self):
        self.driver.get(SIGN_UP_PAGE_URL)

    def fill_user(self, text_user):
        self.driver.find_element(By.NAME, "user").send_keys(text_user)

    def fill_user(self, text_pass):
        self.driver.find_element(By.NAME, "parola").send_keys(text_pass)

    def fill_nume(self, text_nume):
        self.driver.find_element(By.NAME, "nume").send_keys(text_nume)

    def fill_prenume(self, text_prenume):
        self.driver.find_element(By.NAME, "prenume").send_keys(text_prenume)

    def fill_colegiu(self, text_colegiu):
        self.driver.find_element(By.NAME, "colegiu").send_keys(text_colegiu)

    def click_inregistrare(self):
        self.driver.find_element(By.XPATH, '//button[text()="Inregistrare"]').click()

    def verify_signup_url(self, expected_signup_url):
        print(f"url-ul primit: {self.driver.expected_signup_url}")
        import re
        current_url = self.driver.current_url
        if bool(re.match(expected_signup_url, current_url)):
            return 1
        else:
            return 0