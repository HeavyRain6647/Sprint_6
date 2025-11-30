import allure
from pages.main_page import MainPage

class TestRedirects:
    
    @allure.title("Проверка клика по логотипу 'Самокат'")
    @allure.description("При нажатии на логотип Самоката пользователь попадает на главную страницу")
    def test_click_scooter_logo_redirects_to_home(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button() # Переходим на страницу заказа, чтобы было откуда возвращаться
        main_page.click_scooter_logo()
        
        # Проверяем, что вернулись на главную (URL совпадает)
        assert driver.current_url == main_page.URL

    @allure.title("Проверка клика по логотипу 'Яндекс'")
    @allure.description("При нажатии на логотип Яндекса в новом окне открывается Дзен")
    def test_click_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_yandex_logo()
        
        main_page.switch_to_next_tab()
        
        # Яндекс часто редиректит на dzen.ru, ждем загрузки
        main_page.wait_for_url_contains("dzen.ru")
        
        assert "dzen.ru" in driver.current_url