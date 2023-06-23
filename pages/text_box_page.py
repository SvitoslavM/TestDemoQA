from locators.text_box_locators import TextBoxLocators
from pages.base_page import BasePage
from constants import *


class TextBoxPage(BasePage):
    url = "https://demoqa.com/text-box"

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def get_text_text_box(self):
        return self.find_element(TextBoxLocators.GET_TEXT_TEXT_BOX_PAGE_LOCATOR)

    def click_text_box(self):
        text_box_page = self.find_element(TextBoxLocators.TEXT_BOX_LOCATOR)
        text_box_page.click()

    def text_box_f_name(self):
        full_name = self.find_element(TextBoxLocators.TEXT_BOX_FULLNAME_LOCATOR)
        full_name.send_keys(f"{FIRST_NAME} ,{LAST_NAME}")

    def text_box_mail(self):
        mail = self.find_element(TextBoxLocators.TEXT_BOX_MAIL_LOCATOR)
        mail.send_keys(EMAIL)

    def text_box_cur_address(self):
        address = self.find_element(TextBoxLocators.TEXT_BOX_CUR_ADDRESS_LOCATOR)
        address.send_keys(CURRENT_ADDRESS)

    def text_box_perm_address(self):
        p_addres = self.find_element(TextBoxLocators.TEXT_BOX_PERM_ADDRESS_LOCATOR)
        p_addres.send_keys(PERMANENT_ADDRESS)

    def text_box_click_button(self):
        button = self.find_element(TextBoxLocators.TEXT_BOX_BUTTON_SUBM_LOCATOR)
        button.click()
