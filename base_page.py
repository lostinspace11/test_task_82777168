from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.base_url = "https://yandex.ru/"
        self.browser.implicitly_wait(timeout)

    def find_element_on_the_page(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                          message=f"Can't find element: {locator}")

    def find_elements_on_the_page(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator),
                                                          message=f"Can't find elements: {locator}")

    def go_to_main_page(self):
        return self.browser.get(self.base_url)

    def go_to_page(self, url):
        return self.browser.get(url)
