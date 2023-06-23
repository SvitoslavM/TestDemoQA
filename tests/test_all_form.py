from pages.practice_form_page import PracticeForm
import allure


@allure.story('all test in one func')
def test_all_fill_worm(driver):
    page = PracticeForm(driver)
    page.open()
    write_f_name = page.write_text_f_name()
    write_l_name = page.write_text_l_name()
    write_email = page.write_email()
    write_number = page.write_number()
    choice_date = page.change_date_birth()
    driver.execute_script("window.scrollTo(0, 1000);")
    hobbies = page.change_hobbies()
    address = page.write_current_address()
