import allure
from pages.text_box_page import TextBoxPage


@allure.story('Write in fullname')
def test_write_full_name(driver):
    page = TextBoxPage(driver)
    page.open()
    write_full_name = page.text_box_f_name()


@allure.story('Write email')
def test_write_email(driver):
    page = TextBoxPage(driver)
    page.open()
    write_email = page.text_box_mail()


@allure.story('Write current address')
def test_write_cur_address(driver):
    page = TextBoxPage(driver)
    page.open()
    cur_address = page.text_box_cur_address()


@allure.story('Write permanent address')
def test_perm_address(driver):
    page = TextBoxPage(driver)
    page.open()
    perm_address = page.text_box_perm_address()


@allure.story('Click the button')
def test_click_button(driver):
    page = TextBoxPage(driver)
    page.open()
    button = page.text_box_click_button()
