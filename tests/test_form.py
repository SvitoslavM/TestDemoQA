import time
from pages.main_page import MainPage


def test_practice_form(driver):
    page = MainPage(driver)
    page.open()
    click_form_main_page = page.open_form_main_page()
    open_practice_form = click_form_main_page.open_form_page()
    assert open_practice_form.get_text_form_page().text == "Student Registration Form", 'ERROR'

