from pages.practice_form_page import PracticeForm
import allure


class TestFormPage:
    @allure.story('test_fill_form')
    def test_all_fill_form(self, driver):
        form_page = PracticeForm(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        person = form_page.fill_fields_and_submit()
        result = form_page.form_result()
        assert f'{person.fist_name} {person.last_name}' == result[0], 'the form has not been filled'
        assert person.email == result[1], 'the form has not been filled'
