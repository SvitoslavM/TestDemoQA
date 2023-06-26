from selenium.webdriver.common.by import By


class TextBoxLocators:
    text_text_box_page = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div')
    full_name = (By.CSS_SELECTOR, '#userName')
    email = (By.CSS_SELECTOR, '#userEmail')
    current_address = (By.CSS_SELECTOR, '#currentAddress')
    permanent_address = (By.CSS_SELECTOR, '#permanentAddress')
    submit = (By.CSS_SELECTOR, '#submit')

    result_table = (By.XPATH, "//div[@class='border col-md-12 col-sm-12'] //p")

