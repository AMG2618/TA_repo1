import os

from browser import Browser


class BasePage(Browser):
    def find(self, locator):
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def click(self, locator):
        self.find(locator).click()

def get_file_path(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '..', 'resources', filename)
    return os.path.normpath(file_path)