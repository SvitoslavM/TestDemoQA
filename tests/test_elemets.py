from pages.elements_page import ElementsPage
import allure
from pages.main_page import MainPage


def test_elemnts_page(driver):
    page = MainPage(driver)
    page.open()
    go_to_elem = page.open_element_page()
    assert go_to_elem.get_text_text_box().text == "Elements", "Page not found"


def test_test_box_page(driver):
    page = ElementsPage(driver)
    page.open()
    text_box = page.open_text_box_page()
    assert text_box.get_text_text_box().text == "Text Box", 'Page not found 404'
