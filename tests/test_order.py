import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import TestData  # Импорт данных

class TestOrder:
    
    @allure.title("Позитивный сценарий заказа самоката")
    @allure.description("Проверка всего флоу заказа с двумя наборами данных и разными точками входа (верхняя/нижняя кнопка).")
    # Используем данные из data.py
    @pytest.mark.parametrize("is_top, name, surname, address, metro, phone, date, period, color, comment", TestData.ORDER_DATA)
    def test_order_flow(self, driver, is_top, name, surname, address, metro, phone, date, period, color, comment):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_cookie_accept()
        
        # Шаг 1: Клик по кнопке заказа (параметризовано)
        main_page.click_order_button(is_top=is_top)
        
        order_page = OrderPage(driver)
        
        # Шаг 2: Заполнение формы - Шаг 1
        order_page.fill_user_data(name, surname, address, metro, phone)
        # Шаг 3: Заполнение формы - Шаг 2
        order_page.fill_rent_data(date, period, color, comment)
        
        # Шаг 4: Подтверждение
        order_page.confirm_order()
        
        # Шаг 5: Проверка успешного создания заказа
        expected_message = "Заказ оформлен"
        assert expected_message in order_page.get_success_message()