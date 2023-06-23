from pages.base_page import BasePage
from locators.elemets_page_locator import ElementsLocators
from constants import *
from pages.text_box_page import TextBoxPage


class ElementsPage(BasePage):
    url = "https://demoqa.com/elements"

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def open_text_box_page(self):
        open_text_box_page = self.find_element(ElementsLocators.TEXT_BOX_LOCATOR)
        open_text_box_page.click()
        return TextBoxPage(self.driver)
