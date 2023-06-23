from selenium.webdriver.common.by import By


class TextBoxLocators:
    GET_TEXT_TEXT_BOX_PAGE_LOCATOR = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div')
    TEXT_BOX_LOCATOR = (By.XPATH, '//*[@id="item-0"]')
    TEXT_BOX_FULLNAME_LOCATOR = (By.XPATH, '//*[@id="userName"]')
    TEXT_BOX_MAIL_LOCATOR = (By.XPATH, '//*[@id="userEmail"]')
    TEXT_BOX_CUR_ADDRESS_LOCATOR = (By.XPATH, '//*[@id="currentAddress"]')
    TEXT_BOX_PERM_ADDRESS_LOCATOR = (By.XPATH, '//*[@id="permanentAddress"]')
    TEXT_BOX_BUTTON_SUBM_LOCATOR = (By.XPATH, '//*[@id="submit"]')
