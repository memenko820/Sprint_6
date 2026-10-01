import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.main_page import MainPageScooter
from pages.order_page import OrderPageScooter
import constants
import helpers


class TestOrderPage:

    @pytest.mark.parametrize('order_button_position, order_data', [
        (0, 
         {
             'name': helpers.random_name(),
             'surname': helpers.random_name(),
             'address': helpers.random_name(),
             'metro': 'Черкизовская',
             'phone': helpers.random_phone(),
             'order_date': helpers.get_future_date(1),
             'rental_period': 'сутки',
         }),
        (1, 
        {
            'name': helpers.random_name(),
            'surname': helpers.random_name(),
            'address': helpers.random_name(),
            'metro': 'Сокольники',
            'phone': helpers.random_phone(),
            'order_date': helpers.get_future_date(2),
            'rental_period': 'двое суток',
        })
    ])
    @allure.title('Заказ самоката')
    @allure.description('Позитивный сценарий с двумя наборами данных и двумя точками входа: вверху и внизу главной страницы')
    def test_scooter_rental_with_different_enter_points_and_data(self, driver, order_button_position, order_data):

        main_page = MainPageScooter(driver)
        order_page = OrderPageScooter(driver)

        main_page.click_order_button(order_button_position)

        order_page.fill_customer_data(
            order_data['name'],
            order_data['surname'],
            order_data['address'],
            order_data['metro'],
            order_data['phone']
        )

        order_page.click_next_button()

        order_page.fill_rental_data(
            order_data['order_date'],
            order_data['rental_period']
        )

        order_page.click_rental_order_button()
        order_page.click_yes_button()
    
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(order_page.order_success_title)).is_displayed() 

    @allure.title('Переход на главную страницу сайта при клике на логотип "Самокат" в левом верхнем углу экрана')
    @allure.description('Нажимаем на логотип "Самокат" в левом верхнем углу экрана и проверяем, что произошёл переход на главную страницу сайта')
    def test_click_scooter_logo_redirect_to_main_page(self, driver):

        main_page = MainPageScooter(driver)
        order_page = OrderPageScooter(driver)

        main_page.click_order_button(0)
        order_page.click_scooter_logo()

        assert WebDriverWait(driver, 3).until(EC.url_to_be(constants.BASE_URL))