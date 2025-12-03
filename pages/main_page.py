import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urls import Urls # Импортируем Urls

class MainPage(BasePage):
    # Используем URL из urls.py
    URL = Urls.SAMOKAT_HOME_PAGE

    # Локаторы
    LOGO_SCOOTER = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    LOGO_YANDEX = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    
    ORDER_BUTTON_TOP = (By.CLASS_NAME, 'Button_Button__ra12g')
    ORDER_BUTTON_BOTTOM = (By.XPATH, ".//button[contains(@class, 'Button_Middle__1CSd9')]")
    
    COOKIES_BUTTON = (By.ID, 'rcc-confirm-button') # Кнопка куки

    # Метод формирования локатора вопроса по индексу (форматирование строки)
    def get_question_locator(self, num):
        return (By.ID, f"accordion__heading-{num}")

    # Метод формирования локатора ответа по индексу
    def get_answer_locator(self, num):
        return (By.ID, f"accordion__panel-{num}")

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Принять куки")
    def click_cookie_accept(self):
        # ИСПРАВЛЕНО: Вызываем метод из BasePage
        if self.check_element_presence(self.COOKIES_BUTTON): 
            self.click_element(self.COOKIES_BUTTON)

    @allure.step("Кликнуть по вопросу в FAQ")
    def click_faq_question(self, num):
        locator = self.get_question_locator(num)
        self.click_element(locator)

    @allure.step("Получить текст ответа")
    def get_faq_answer_text(self, num):
        locator = self.get_answer_locator(num)
        return self.get_text(locator) # Используем get_text из BasePage

    @allure.step("Кликнуть кнопку 'Заказать' (верхнюю или нижнюю)")
    def click_order_button(self, is_top=True):
        if is_top:
            self.click_element(self.ORDER_BUTTON_TOP)
        else:
            self.click_element(self.ORDER_BUTTON_BOTTOM)

    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(self.LOGO_SCOOTER)

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(self.LOGO_YANDEX)