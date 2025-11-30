import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderPage(BasePage):
    # Локаторы 1 шага
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.CLASS_NAME, "select-search__input")
    METRO_OPTION_TEMPLATE = "//div[@class='select-search__select']//*[text()='{}']" # Динамический
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локаторы 2 шага
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_PERIOD_OPTION_TEMPLATE = "//div[@class='Dropdown-menu']/div[text()='{}']"
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON_FINAL = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    
    # Модалка подтверждения
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")

    @allure.step("Заполнить первый шаг формы заказа")
    def fill_user_data(self, name, surname, address, metro_name, phone):
        self.set_text(self.NAME_INPUT, name)
        self.set_text(self.SURNAME_INPUT, surname)
        self.set_text(self.ADDRESS_INPUT, address)
        
        self.click_element(self.METRO_FIELD)
        metro_locator = (By.XPATH, self.METRO_OPTION_TEMPLATE.format(metro_name))
        self.click_element(metro_locator)
        
        self.set_text(self.PHONE_INPUT, phone)
        self.click_element(self.NEXT_BUTTON)

    @allure.step("Заполнить второй шаг формы заказа")
    def fill_rent_data(self, date, period, color, comment):
        self.set_text(self.DATE_FIELD, date)
        # Клик по body или Enter, чтобы закрыть календарь, но проще кликнуть на след. поле
        self.click_element(self.RENTAL_PERIOD_FIELD)
        period_locator = (By.XPATH, self.RENTAL_PERIOD_OPTION_TEMPLATE.format(period))
        self.click_element(period_locator)
        
        if color == 'black':
            self.click_element(self.COLOR_BLACK)
        elif color == 'grey':
            self.click_element(self.COLOR_GREY)
            
        self.set_text(self.COMMENT_FIELD, comment)
        self.click_element(self.ORDER_BUTTON_FINAL)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_element(self.YES_BUTTON)

    @allure.step("Получить текст заголовка успешного заказа")
    def get_success_message(self):
        return self.get_text(self.SUCCESS_MODAL_HEADER)