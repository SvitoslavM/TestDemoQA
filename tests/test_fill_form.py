from pages.practice_form_page import PracticeForm
import allure

@allure.story("Write first name in name")
def test_write_f_name(driver):
    page = PracticeForm(driver)
    page.open()
    write_f_name = page.write_text_f_name()

@allure.story("write last name in name")
def test_write_l_name(driver):
    page = PracticeForm(driver)
    page.open()
    write_l_name = page.write_text_l_name()

@allure.story("Write email in filt meail")
def test_write_email(driver):
    page = PracticeForm(driver)
    page.open()
    write_email = page.write_email()
# @allure.story("")
# @allure.story("")
# @allure.story("")
# @allure.story("")
# @allure.story("")
# @allure.story("")
# @allure.story("")

