import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features.pages.base_page import BasePage

USER_PAGE = "https://probaamg.rdsweb.ro/user/\d+$"

class UploadDocumentPage(BasePage):
    BUTTON_INCARCA_FISIER = (By.LINK_TEXT, 'Incarca fisier')
    CHOOSE_FILE_BUTTON = (By.NAME, "file")
    # INPUT_FILE = (By.NAME, "file")
    INPUT_TIP = (By.ID, "tip")
    PUNCTE_EMC = (By.NAME, "emc")
    INPUT_DATE = (By.NAME, "data")
    BUTTON_INCARCA = (By.XPATH, '//input[@type="submit" and @value="Incarca"]')
    UPLOAD_MESSAGE = (By.XPATH, "//p[contains(text(), 'A fost incarcat: Test_documente_incarcate.pdf de tipul diploma_emc')]")

    def open(self):
        self.driver.get(USER_PAGE)

    def click_incarca_fisier_link(self):
        self.click(self.BUTTON_INCARCA_FISIER)

    def get_file_path(self, filename):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, '..', 'resources', filename)
        return os.path.normpath(file_path)

    def choose_file(self, get_file_path):
        self.driver.find_element(*self.CHOOSE_FILE_BUTTON).send_keys(get_file_path)

    # def choose_file(self, file_path):
    #     self.driver.find_element(*self.CHOOSE_FILE_BUTTON).send_keys(file_path)
    #
    #
    # def upload_file_path(self):
    #     self.driver.find_element(*self.CHOOSE_FILE_BUTTON).send_keys(self.FILE_PATH)

    def select_tip_document(self, text_document):
        dropdown = Select(self.driver.find_element(By.ID, "tip"))
        dropdown.select_by_value("diploma_emc")

    def select_emc(self, text_emc):
        dropdown = Select(self.driver.find_element(By.NAME, "emc"))
        dropdown.select_by_value(text_emc)

    def select_date(self, date_text):
        self.driver.find_element(*self.INPUT_DATE).send_keys(date_text)

    def click_button_submit(self):
        self.click(self.BUTTON_INCARCA)

    def verify_document_upload_success(self, text_succes):
        success_message = self.driver.find_element(By.XPATH, "//p[contains(text(), 'A fost incarcat: Test_documente_incarcate.pdf de tipul diploma_emc')]").text
        return success_message is not None






