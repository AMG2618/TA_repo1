from selenium.webdriver.common.by import By

from browser import Browser

LOGIN_PAGE_URL = "https://probaamg.rdsweb.ro/login"

class LoginPage(Browser):

    INPUT_USERNAME = (By.NAME, "username")
    INPUT_PASSWORD = (By.NAME, "password")
    BUTTON_SUBMIT = (By.XPATH, "//input[@type='submit' and @value='Conectare']")

    def open(self):
        self.driver.get(LOGIN_PAGE_URL)

    def set_username(self, text):
        self.driver.find_element(*self.INPUT_USERNAME).send_keys(text)

    def set_password(self, pass_text):
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys(pass_text)

    def click_button_submit(self):
        self.driver.find_element(*self.BUTTON_SUBMIT).click()

    def verify_current_url(self, expected_url):
        print(f"url-ul primit: {self.driver.current_url}" )
        import re
        current_url = self.driver.current_url
        if bool (re.match(expected_url, current_url)):
            return 1
        else:
            return 0
        # return self.driver.current_url == expected_url

