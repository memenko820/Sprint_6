import allure
from selenium.webdriver.common.by import By


# Класс для главной страницы
class MainPageScooter:
    yandex_logo = (By.XPATH, '//img[@alt="Yandex"]')
    order_buttons = (By.XPATH, '//button[text()="Заказать"]')
    cookie_button = (By.XPATH, '//button[text()="да все привыкли"]')

    # Раздел FAQ: коллекции вопросов и ответов
    faq_questions = (By.XPATH, '//*[starts-with(@id, "accordion__heading-") and @role="button"]')
    faq_answers = (By.XPATH, '//*[starts-with(@id, "accordion__panel-") and @role="region"]')

    def __init__(self, driver):
        self.driver = driver

    def click_faq_question(self, num):
        with allure.step(f'Нажимаем на вопрос №{num + 1}'):
            questions = self.driver.find_elements(*self.faq_questions)
            questions[num].click()
    
    def get_faq_answer_text(self, num):
        with allure.step(f'Получаем текст ответа для вопроса №{num + 1}'):
            answers = self.driver.find_elements(*self.faq_answers)
            return answers[num].text

    @allure.step('Принимаем cookie')
    def click_cookie_button(self):
        self.driver.find_element(*self.cookie_button).click()

    def click_order_button(self, button_index):
        button_positions = {
            0: 'вверху страницы',
            1: 'внизу страницы'
        }

        with allure.step(
            f'Нажимаем кнопку «Заказать» {button_positions[button_index]}'
        ):
            buttons = self.driver.find_elements(*self.order_buttons)
            buttons[button_index].click()

    @allure.step('Нажимаем на логотип "Яндекс" в левом верхнем углу страницы')
    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()