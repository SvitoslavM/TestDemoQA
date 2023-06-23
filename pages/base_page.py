from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(
                locator)
            )
            return element
        except TimeoutException:
            message = f"Can't find elements by locator {locator}"

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}")
