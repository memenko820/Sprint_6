import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Класс для описания страницы заказов
class OrderPageScooter:

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

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполняем поле "Имя" на экране "Для кого самокат"')
    def fill_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    @allure.step('Заполняем поле "Фамилия" на экране "Для кого самокат"')
    def fill_surname(self, surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    @allure.step('Заполняем поле "Адрес" на экране "Для кого самокат"')
    def fill_address(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    @allure.step('Выбираем станцию метро на экране "Для кого самокат"')
    def select_metro_station(self, station_name):
        self.driver.find_element(*self.metro_field).click()
        station = (By.XPATH, f'//*[text()="{station_name}"]')
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(station)).click()

    @allure.step('Заполняем поле "Телефон" на экране "Для кого самокат"')
    def fill_phone(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    @allure.step('Нажимаем кнопку "Далее" на экране "Для кого самокат"')
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    @allure.step('Заполняем поле "Когда привезти самокат" на экране "Про аренду"')
    def fill_order_date(self, future_date):
        field = self.driver.find_element(*self.order_date_field)
        field.send_keys(future_date)
        field.send_keys(Keys.ENTER)

    @allure.step('Выбираем "Срок аренды" на экране "Про аренду"')
    def select_rental_period_option(self, period):
        self.driver.find_element(*self.rental_period_field).click()
        self.driver.find_element(By.XPATH, f'//div[@role="option" and text()="{period}"]').click()

    @allure.step('Нажимаем кнопку "Заказать" на экране "Про аренду"')
    def click_rental_order_button(self):
        self.driver.find_element(*self.rental_order_button).click()

    @allure.step('Нажимаем кнопку "Да" в модальном окне "Хотите оформить заказ"')
    def click_yes_button(self):
        self.driver.find_element(*self.yes_button).click()

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
        self.driver.find_element(*self.scooter_logo).click()
        