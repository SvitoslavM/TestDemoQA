import random
import requests
import allure
from selenium.webdriver.common.by import By

from locators.elements_page_locators import TextBoxLocators, CheckBoxPageLocators, RadioPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person


class TextBoxPage(BasePage):
    locators = TextBoxLocators

    @allure.step("Fill in all fields")
    def text_box_form(self):
        self.remove_footer()
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        with allure.step('filing fields'):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step('click submit button'):
            self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step('check filled form')
    def check_filled_form(self):
        full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step('open full list')
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step('click random items')
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    # use refactor text from results(data)
    @allure.step('get checked checkbox')
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    # use refactor text from results(data)
    @allure.step('get checked checkbox')
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioPageLocators

    @allure.step('click on the radiobutton')
    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                   'no': self.locators.NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    @allure.step('get output result')
    def get_out_put_result_radiobutton(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators

    @allure.step('add new person')
    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.fist_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_clickable(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_clickable(self.locators.SUBMIT).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    @allure.step('check added people')
    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    @allure.step('find some person')
    def search_some_people(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.step('check found person')
    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element('xpath', self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step('update person information')
    def update_person_info(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            fistname = person_info.fist_name
            lastname = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_clickable(self.locators.UPDATE_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).clear()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(fistname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).clear()
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).clear()
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).clear()
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).clear()
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).clear()
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_clickable(self.locators.SUBMIT).click()
            count -= 1
            return [fistname, lastname, str(age), email, str(salary), department]

    @allure.step('delete person')
    def delete_person(self):
        self.element_is_clickable(self.locators.DELETE_BUTTON).click()

    @allure.step('check deleted person')
    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.step('select up to some rows')
    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())
        return data

    @allure.step('check count rows')
    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonPage(BasePage):
    locators = ButtonsPageLocators

    @allure.step('Double click')
    def click_on_double_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)

    @allure.step('Right click')
    def click_on_right_button(self, type_click):
        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)

    @allure.step("Click me or dynamic click")
    def click_on_dynamic_button(self, type_click):
        if type_click == "click":
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)

    @allure.step('check clicked button')
    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = LinksPageLocators

    @allure.step('check home link')
    def check_home_simple_link(self):
        simpl_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simpl_link.get_attribute('href')
        r = requests.get(link_href)
        if r.status_code == 200:
            simpl_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, r.status_code

    @allure.step('check dynamic link')
    def check_home_dynamic_link(self):
        dynamic_link = self.element_is_visible(self.locators.DYNAMIC_LINK)
        link_href = dynamic_link.get_attribute('href')
        r = requests.get(link_href)
        if r.status_code == 200:
            dynamic_link.click()
            # self.driver.switch_to.window(self.driver.window_handles[1]) -- for switch another page
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, r.status_code

    @allure.step('check created link')
    def check_created_link(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            self.element_is_present(self.locators.CREATED_LINK).click()
        else:
            return r.status_code

    @allure.step('check no content link')
    def check_no_content_link(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            self.element_is_present(self.locators.NO_CONTENT_LINK).click()
        else:
            return r.status_code

    @allure.step('check moved link')
    def check_moved_link(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            self.element_is_present(self.locators.MOVED_LINK).click()
        else:
            return r.status_code

    @allure.step('check bad request link')
    def check_broken_link_by_bad_request(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST).click()
        else:
            return r.status_code

    @allure.step('check unauthorized link')
    def check_unauthorized_link(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            self.element_is_present(self.locators.UNAUTHORIZED_LINK).click()
        else:
            return r.status_code

    @allure.step('check forbidden link')
    def check_forbidden_link(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            self.element_is_present(self.locators.FORBIDDEN_LINK).click()
        else:
            return r.status_code

    @allure.step('check not found link')
    def check_not_found_link(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            self.element_is_present(self.locators.NOT_FOUND_LINK).click()
        else:
            return r.status_code
