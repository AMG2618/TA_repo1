from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features.pages.base_page import BasePage

USER_PAGE = "https://probaamg.rdsweb.ro/user/\d+$"

class UploadDocumentPage(BasePage):

    CLICK_LINK = (By.XPATH, "//input[@type='submit' and @value='Incarca fisier']")
    CHOOSE_FILE_BUTTON = (By.NAME, "file")
    FILE_PATH = r"C:\\Users\Localadmin\Downloads/Test documente incarcate.pdf"
    INPUT_TIP_DOCUMENT = (By.ID, "tip")
    PUNCTE_EMC = (By.ID, "emc")
    INPUT_DATE = (By.NAME, "data")
    BUTTON_INCARCA = (By.XPATH, "//input[@type='submit' and @value='Incarca']")
    UPLOAD_MESSAGE = (By.XPATH, "//p[contains(text(), 'A fost incarcat: Test_documente_incarcate.pdf de tipul diploma_emc')]")

    def open(self):
        self.driver.get(USER_PAGE)

    def click_incarca_fisier_link(self):
        user_id = self.driver.find_element(By.XPATH, '//td[contains(text(), "ID")]/following-sibling::td').text
        self.driver.find_element(By.XPATH, f'//a[contains(@href, "/incarcare/{user_id}")]').click()

    def choose_file(self, file_path):
        self.driver.find_element(*self.CHOOSE_FILE_BUTTON).send_keys(file_path)

    def upoad_file_path(self):
        self.driver.find_element(*self.FILE_INPUT).send_keys(self.FILE_PATH)

    def select_tip_document(self):
        dropdown = Select(self.driver.find_element(By.ID, "tip"))
        dropdown.select_by_value(("diploma_emc"))

    def select_emc(self):
        dropdown = Select(self.driver.find_element(By.ID, "emc"))
        dropdown.select_by_value("24")

    def select_date(self, date_text):
        self.driver.find_element(*self.INPUT_DATE).send_keys("08/13/2025")

    def click_button_submit(self):
        self.click(self.BUTTON_INCARCA)

    def verify_document_upload_success(self):
        success_message = self.driver.find_element(By.XPATH, "//p[contains(text(), 'A fost incarcat: Test_documente_incarcate.pdf de tipul diploma_emc')]").text
        return success_message is not None






