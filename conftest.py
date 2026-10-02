import pytest
from selenium import webdriver
from pages.main_page import MainPageScooter
import constants


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    main_page = MainPageScooter(driver)

    main_page.open_page(constants.BASE_URL)
    main_page.click_cookie_button()

    yield driver

    driver.quit()
