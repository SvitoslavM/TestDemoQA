from pages.base_page import BasePage
from locators.practice_form_locators import PracticeFormLocators
from constants import *


class PracticeForm(BasePage):
    url = "https://demoqa.com/automation-practice-form/"

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def get_text_form_page(self):
        return self.find_element(PracticeFormLocators.GET_TEXT_FORM_PAGE_LOCATOR)

    def write_text_f_name(self):
        text = self.find_element(PracticeFormLocators.WRITE_FIRST_NAME_LOCATOR)
        text.send_keys(FIRST_NAME)

    def write_text_l_name(self):
        text = self.find_element(PracticeFormLocators.WRITE_LAST_NAME_LOCATOR)
        text.send_keys(LAST_NAME)

    def write_email(self):
        email = self.find_element(PracticeFormLocators.WRITE_EMAIL_LOCATOR)
        email.send_keys(EMAIL)

    def change_gender(self):
        button = self.find_element(PracticeFormLocators.CHOICE_GENDER_LOCATOR)
        button.click()

    def change_date_birth(self):
        button = self.find_element(PracticeFormLocators.CLICK_ON_DATE_BIRTH_LOCATOR)
        button.click()
        change_date = self.find_element(PracticeFormLocators.CHOICE_DATE_BIRTH_LOCATOR)
        change_date.click()

    def change_hobbies(self):
        hobbies = self.find_element(PracticeFormLocators.SELECT_HOBBIES_LOCATOR)
        hobbies.click()

    def write_current_address(self):
        address = self.find_element(PracticeFormLocators.ClICK_CURRENT_ADDRESS_LOCATOR)
        address.click()
        address_message = self.find_element(PracticeFormLocators.ClICK_CURRENT_ADDRESS_LOCATOR)
        address_message.send_keys(CURRENT_ADDRESS)

    def write_number(self):
        number = self.find_element(PracticeFormLocators.WHITE_MOBILE_LOCATOR)
        number.send_keys(MOBILE)
