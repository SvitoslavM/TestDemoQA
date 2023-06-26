from locators.text_box_locators import TextBoxLocators as Locator
from pages.base_page import BasePage
from generator.generator import generated_person


class TextBoxPage(BasePage):

    def get_text_text_box(self):
        return self.element_is_visible(Locator.text_text_box_page)

    def text_box_form(self):
        person = generated_person()
        self.remove_footer()
        self.element_is_visible(Locator.full_name).send_keys(f'{person.fist_name}  {person.last_name}')
        self.element_is_visible(Locator.email).send_keys(person.email)
        self.element_is_visible(Locator.current_address).send_keys(person.current_address)
        self.element_is_visible(Locator.permanent_address).send_keys(person.permanent_address)
        self.element_is_visible(Locator.submit).click()
        return person

    def text_box_result(self):
        result_list = self.elements_are_visible(Locator.result_table)
        text_box_text = [i.text for i in result_list]
        return text_box_text

    def text_box_mail(self):
        result_list = self.elements_are_visible(Locator.result_email)
        text_box_email = [i.text for i in result_list]
        return text_box_email