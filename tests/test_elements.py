import random
import time

import allure

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonPage, LinksPage


@allure.suite("Elements")
class TestElements:
    @allure.feature('TextBox')
    class TestTextBox:
        @allure.title('Check TextBox')
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.text_box_form()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, 'the full name does not match'
            assert email == output_email, 'the email does not match'
            assert current_address == output_cur_addr, 'the current address does not match'
            assert permanent_address == output_per_addr, 'the permanent does not match'

    @allure.feature('CheckBox')
    class TestCheckBox:
        @allure.title('Check CheckBox')
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_check_box = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_check_box == output_result, 'checkboxes have not been selected'

    @allure.feature('RadioButton')
    class TestRadioButton:
        @allure.title('Check RadioButton')
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_out_put_result_radiobutton()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_out_put_result_radiobutton()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_out_put_result_radiobutton()
            with allure.story('Test output "yes"'):
                assert output_yes == 'Yes', "'Yes' have not been selected"
            with allure.story('Test output "impressive"'):
                assert output_impressive == "Impressive", "'Impressive' have not been selected"
            with allure.story("test output 'No'"):
                assert output_no == 'No', "'No' have not been selected"

    @allure.feature("WebTable")
    class TestWebTable:
        @allure.title('Check to add a person to the table')
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            input_new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert input_new_person in table_result

        @allure.title('Check to search person in table')
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            time.sleep(0.2)
            web_table_page.search_some_people(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "the person was not found in the table"

        @allure.title('Checking to update the persons info in the table')
        def test_webtable_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_people(key_word)
            some_word = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert some_word == row, "the person card has not been changed"

        @allure.title('Checking to remove a person from the table')
        def test_webtable_delete_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            time.sleep(0.5)
            web_table_page.search_some_people(key_word)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == 'No rows found'

        @allure.title('Check the change in the number of rows in the table')
        def test_webtable_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], "the numbers or rows in the table has not been changed or has changed incorrectly"

    @allure.feature("Buttons")
    class TestButtonsPage:

        @allure.title("Click on double click button")
        def test_double_click_button(self, driver):
            button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_double_button('double')
            assert double == "You have done a double click", 'The double click button was not pressed'

        @allure.title(
            "Click on right click button")
        def test_right_click_button(self, driver):
            button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            right = button_page.click_on_right_button('right')
            assert right == "You have done a right click", 'The right click button was not pressed'

        @allure.title(
            "Click on dynamic button")
        def test_dynamic_click_button(self, driver):
            button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            click = button_page.click_on_dynamic_button('click')
            print(click)
            assert click == "You have done a dynamic click", 'The dynamic click button was not pressed'

    @allure.feature("Links")
    class TestLinksPage:
        @allure.title("test home link")
        def test_home_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_home_simple_link()
            assert href_link == current_url, "the link is broken or url is incorrect"

        @allure.title("test dynamic link")
        def test_dynamic_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_home_dynamic_link()
            assert href_link == current_url, 'the link is broken or url is incorrect'

        @allure.title("test created link get status code 201")
        def test_created_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_created_link('https://demoqa.com/Created')
            assert response_code == 201, 'the link works or the status code in son 201'

        @allure.title("test no content link get status code 204")
        def test_no_content_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_no_content_link('https://demoqa.com/No-Content')
            assert response_code == 204, 'the link works or the status code in son 204'

        @allure.title("test moved link get status code 301")
        def test_moved_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_moved_link('https://demoqa.com/Moved')
            assert response_code == 301, 'the link works or the status code in son 301'

        @allure.title("test bad request link get status code 400")
        def test_bad_request_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link_by_bad_request('https://demoqa.com/bad-request')
            assert response_code == 400, 'the link works or the status code in son 400'

        @allure.title("test unauthorized link get status code 401")
        def test_unauthorized_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_unauthorized_link('https://demoqa.com/Unauthorized')
            assert response_code == 401, 'the link works or the status code in son 401'

        @allure.title("test forbidden link get status code 403")
        def test_forbidden_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_unauthorized_link('https://demoqa.com/Forbidden')
            assert response_code == 403, 'the link works or the status code in son 403'

        @allure.title("test not found link get status code 404")
        def test_not_found_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_not_found_link('https://demoqa.com/invalid-url')
            assert response_code == 404, 'the link works or the status code in son 404'
