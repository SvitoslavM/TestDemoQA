from pages.base_page import BasePage
from locators.practice_form_locators import PracticeFormLocators


class PracticeForm(BasePage):
    url = "https://demoqa.com/automation-practice-form/"

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def get_text_form_page(self):
        return self.find_element(PracticeFormLocators.GET_TEXT_FORM_PAGE_LOCATOR)
