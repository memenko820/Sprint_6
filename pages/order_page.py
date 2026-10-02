import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


# Класс для описания страницы заказов
class OrderPageScooter(BasePage):

    scooter_logo = (By.XPATH, '//img[@alt="Scooter"]')
    # Поля "Для кого самокат"
    name_field = (By.XPATH, '//input[contains(@placeholder, "Имя")]')
    surname_field = (By.XPATH, '//input[contains(@placeholder, "Фамилия")]')
    address_field = (By.XPATH, '//input[contains(@placeholder, "Адрес")]')
    metro_field = (By.XPATH, '//input[contains(@placeholder, "Станция метро")]')
    phone_field = (By.XPATH, '//input[contains(@placeholder, "Телефон")]')
    next_button = (By.XPATH, '//button[text()="Далее"]')

    # Поля "Про аренду"
    order_date_field = (By.XPATH, '//input[contains(@placeholder, "Когда привезти")]')
    rental_period_field = (By.XPATH, '//div[contains(text(), "Срок аренды")]')
    rental_order_button = (By.XPATH, '//button[contains(@class, "Middle") and text()="Заказать"]')

    # Модальное окно "Хотите оформить заказ?"
    yes_button = (By.XPATH, '//button[text()="Да"]')

    # Модальное окно "Заказ оформлен"
    order_success_title = (By.XPATH, '//div[text()="Заказ оформлен"]')

    @allure.step('Заполняем поле "Имя" на экране "Для кого самокат"')
    def fill_name(self, name):
        self.fill_input(self.name_field, name)

    @allure.step('Заполняем поле "Фамилия" на экране "Для кого самокат"')
    def fill_surname(self, surname):
        self.fill_input(self.surname_field, surname)

    @allure.step('Заполняем поле "Адрес" на экране "Для кого самокат"')
    def fill_address(self, address):
        self.fill_input(self.address_field, address)

    @allure.step('Выбираем станцию метро на экране "Для кого самокат"')
    def select_metro_station(self, station_name):
        self.click_element(self.metro_field)
        station = (By.XPATH, f'//*[text()="{station_name}"]')
        self.wait_and_click_element(station)

    @allure.step('Заполняем поле "Телефон" на экране "Для кого самокат"')
    def fill_phone(self, phone):
        self.fill_input(self.phone_field, phone)

    @allure.step('Нажимаем кнопку "Далее" на экране "Для кого самокат"')
    def click_next_button(self):
        self.click_element(self.next_button)

    @allure.step('Заполняем поле "Когда привезти самокат" на экране "Про аренду"')
    def fill_order_date(self, future_date):
        self.fill_input(self.order_date_field, future_date)
        self.press_key(self.order_date_field, Keys.ENTER)

    @allure.step('Выбираем "Срок аренды" на экране "Про аренду"')
    def select_rental_period_option(self, period):
        self.click_element(self.rental_period_field)
        period_option = (By.XPATH, f'//div[@role="option" and text()="{period}"]')
        self.click_element(period_option)

    @allure.step('Нажимаем кнопку "Заказать" на экране "Про аренду"')
    def click_rental_order_button(self):
        self.click_element(self.rental_order_button)

    @allure.step('Нажимаем кнопку "Да" в модальном окне "Хотите оформить заказ"')
    def click_yes_button(self):
        self.click_element(self.yes_button)

    # Верхнеуровневый метод для заполнения страницы "Для кого самокат"
    def fill_customer_data(self, name, surname, address, metro, phone):
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.select_metro_station(metro)
        self.fill_phone(phone)

    # Верхнеуровневый метод для заполнения страницы "Про аренду"
    def fill_rental_data(self, order_date, rental_period):
        self.fill_order_date(order_date)
        self.select_rental_period_option(rental_period)

    @allure.step('Нажимаем на логотип "Самокат" в левом верхнем углу страницы')
    def click_scooter_logo(self):
        self.click_element(self.scooter_logo)

    @allure.step('Проверяем отображение сообщения об успешном оформлении заказа')
    def is_order_success_message_displayed(self):
        return self.is_element_visible(self.order_success_title)
        