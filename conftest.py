import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPageScooter
import constants

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    main_page = MainPageScooter(driver)
    driver.get(constants.BASE_URL)
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(main_page.cookie_button))
    main_page.click_cookie_button()
    
    yield driver

    driver.quit()
