from pages.main_page import MainPage
import allure


@allure.story('Open main page')
def test_practice_form(driver):
    with allure.step('Open main page'):
        page = MainPage(driver)
    page.open()
    with allure.step('click on form page, then on form page click on practice rorm '):
        click_form_main_page = page.open_form_main_page()
    open_practice_form = click_form_main_page.open_form_page()
    with allure.step("go to test practice form text"):
        assert open_practice_form.get_text_form_page().text == "Student Registration Form", 'ERROR'