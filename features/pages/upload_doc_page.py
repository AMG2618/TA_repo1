import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from features.pages.base_page import BasePage

USER_PAGE = "https://probaamg.rdsweb.ro/user"

class UploadDocumentPage(BasePage):
    BUTTON_INCARCA_FISIER = (By.LINK_TEXT, 'Incarca fisier')
    CHOOSE_FILE_BUTTON = (By.NAME, "file")
    INPUT_TIP = (By.ID, "tip")
    PUNCTE_EMC = (By.NAME, "emc")
    INPUT_DATE = (By.NAME, "data")
    BUTTON_INCARCA = (By.XPATH, '//input[@type="submit" and @value="Incarca"]')

    def open(self):
        self.driver.get(USER_PAGE)

    def click_incarca_fisier_link(self):
        self.click(self.BUTTON_INCARCA_FISIER)

    def get_file_path(self, filename):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, '..', 'resources', filename)
        return os.path.normpath(file_path)

    def choose_file(self, file_path):
        print("Calea trimisă către input:", file_path)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Fișierul nu a fost găsit la calea: {file_path}")
        self.driver.find_element(*self.CHOOSE_FILE_BUTTON).send_keys(file_path)

    def select_tip_document(self, text_document):
        dropdown = Select(self.driver.find_element(*self.INPUT_TIP))
        dropdown.select_by_visible_text(text_document)

    def select_emc(self, text_emc):
        dropdown = Select(self.driver.find_element(*self.PUNCTE_EMC))
        dropdown.select_by_visible_text(text_emc)

    def select_date(self, date_text):
        self.driver.find_element(*self.INPUT_DATE).send_keys(date_text)

    def click_button_submit(self):
        self.click(self.BUTTON_INCARCA)

    def verify_document_upload_success(self, filename, tip_document):
        tip_format = tip_document.lower().replace(" ", "_")
        xpath = f"//p[contains(text(), 'A fost incarcat: {filename} de tipul {tip_format}')]"
        return self.driver.find_element(By.XPATH, xpath).is_displayed()







