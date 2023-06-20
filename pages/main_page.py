from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from pages.page_demo_forms import DemoqaPageForms


# from locators.practice_form_locators import M


class MainPage(BasePage):
    url = "https://demoqa.com/"

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def open_form_main_page(self):
        click_form_from_main_page = self.find_element(MainPageLocators.CLICK_FORM_FROM_MAIN_PAGE_LOCATOR)
        click_form_from_main_page.click()
        return DemoqaPageForms(self.driver)

