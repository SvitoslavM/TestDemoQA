import time

from pages.base_page import BasePage
from locators.page_demo_forms_locators import DemoqaFormsLocators
from pages.practice_form_page import PracticeForm


class DemoqaPageForms(BasePage):
    url = "https://demoqa.com/forms"

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def open_form_page(self):
        open_from = self.find_element(DemoqaFormsLocators.OPEN_PRACTICE_FORM_LOCATOR)
        open_from.click()
        return PracticeForm(self.driver)
