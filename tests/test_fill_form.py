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


@allure.story("Write mobile number")
def test_write_mobile(driver):
    page = PracticeForm(driver)
    page.open()
    write_number = page.write_number()


@allure.story("change date of birthday 17 jun 2023")
def test_choice_date_of_birth(driver):
    page = PracticeForm(driver)
    page.open()
    choice_date = page.change_date_birth()


@allure.story("Press button to change hobbies")
def test_change_hobbies(driver):
    page = PracticeForm(driver)
    page.open()
    hobbies = page.change_hobbies()


@allure.story("Write current address in 'Current Address'")
def test_write_current_address(driver):
    page = PracticeForm(driver)
    page.open()
    # driver.execute_script("document.body.style.zoom='67%'")
    driver.execute_script("window.scrollTo(0, 1000);")
    address = page.write_current_address()


