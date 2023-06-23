from pages.base_page import BasePage
from locators.practice_form_locators import PracticeFormLocators
from constants import *


class ElementsPage(BasePage):
    url = "https://demoqa.com/elements"

    def __init__(self, driver):
        super().__init__(driver, self.url)
