from pages.text_box_page import TextBoxPage


class TestTextBox:
    def test_text_box(self, driver):
        text_box = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box.open()
        person = text_box.text_box_form()
        result = text_box.text_box_result()
        # get_text = text_box.get_text_text_box()
        print(person)
        print(result)
        assert f'Name:{person.fist_name} {person.last_name}' == result[0]
        assert f'Email:{person.email}' == result[1]
