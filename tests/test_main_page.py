import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.main_page import MainPageScooter
import constants


class TestMainPage:

    @pytest.mark.parametrize('question_index, expected_answer', [
        (0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ])
    @allure.title('Открытие соответствующего текста при клике на вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на вопрос и проверяем, что отображается соответствующий текст ответа')
    def test_get_faq_answer_by_click_faq_question(self, driver, question_index, expected_answer):

        main_page = MainPageScooter(driver)

        main_page.click_faq_question(question_index)
        actual_answer = main_page.get_faq_answer_text(question_index)

        assert actual_answer == expected_answer

    @allure.title('Переход на "ya.ru" при клике на логотип "Яндекса" на главной странице')
    @allure.description('Нажимаем на логотип "Яндекса" в левом верхнем углу экрана и проверяем, что произошёл переход на "ya.ru" в новом окне браузера')
    def test_click_yandex_logo_redirect_to_yandex_page(self, driver):

        main_page = MainPageScooter(driver)

        main_page.click_yandex_logo()
        WebDriverWait(driver, 3).until(EC.number_of_windows_to_be(2))

        driver.switch_to.window(driver.window_handles[1])

        print(driver.current_url)

        assert WebDriverWait(driver, 5).until(EC.url_to_be(constants.YANDEX_PAGE))
