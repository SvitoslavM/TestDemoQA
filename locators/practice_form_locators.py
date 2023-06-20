from selenium.webdriver.common.by import By


class PracticeFormLocators:
    WRITE_FIRST_NAME_LOCATOR = (By.XPATH, '//*[@id="firstName"]')
    WRITE_LAST_NAME_LOCATOR = (By.XPATH, '//*[@id="lastName"]')
    WRITE_EMAIL_LOCATOR = (By.XPATH, '//*[@id="userEmail"]')
    CHOICE_GENDER_LOCATOR = (By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]/label')
    WHITE_MOBILE_LOCATOR = (By.XPATH, '//*[@id="userNumber"]')
    CLICK_ON_DATE_BIRTH_LOCATOR = (By.XPATH, '//*[@id="dateOfBirthInput"]')
    CHOICE_DATE_BIRTH_LOCATOR = (By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[4]')
    CLICK_SUBJECTS_LOCATOR = (By.XPATH, '//*[@id="subjectsContainer"]/div/div[1]')
    CHOICE_SUBJECTS_LOCATOR = (By.XPATH, '//*[@id="subjectsContainer"]/div')
    SELECT_HOBBIES_LOCATOR = (By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[3]/label')
    ClICK_CURRENT_ADDRESS_LOCATOR = (By.XPATH, '//*[@id="currentAddress"]')
    CLICK_STATE_CHOICE_STATE = (By.XPATH, '//*[@id="state"]/div/div[1]')
    SELECT_NCR_IN_STATE_MENU_LOCATOR = (By.XPATH, '//*[@id="state"]/div/div[1]/div[1]')
    CLICK_CITY_IN_STATE_LOCATOR = (By.XPATH, '//*[@id="city"]/div/div[1]')
    SELECT_GUARGON_IN_CITY_LOCATOR = (By.XPATH, '//*[@id="city"]/div/div[1]/div[1]')
    GET_TEXT_FORM_PAGE_LOCATOR = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/h5')
