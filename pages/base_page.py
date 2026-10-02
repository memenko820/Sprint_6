from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Страница-родитель с базовыми методами
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        self.find_element(locator).click()

    def fill_input(self, locator, text):
        self.find_element(locator).send_keys(text)

    def wait_and_click_element(self, locator):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator)).click()

    def press_key(self, locator, key):
        self.find_element(locator).send_keys(key)

    def switch_to_new_window(self):
        WebDriverWait(self.driver, 3).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_for_url(self, url):
        return WebDriverWait(self.driver, 5).until(EC.url_to_be(url))

    def is_element_visible(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).is_displayed()

    def open_page(self, url):
        self.driver.get(url)