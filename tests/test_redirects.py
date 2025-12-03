import allure
from pages.main_page import MainPage
from urls import Urls # Импортируем Urls

class TestRedirects:
    
    @allure.title("Проверка клика по логотипу 'Самокат'")
    @allure.description("При нажатии на логотип Самоката пользователь попадает на главную страницу")
    def test_click_scooter_logo_redirects_to_home(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button() # Переходим на страницу заказа, чтобы было откуда возвращаться
        main_page.click_scooter_logo()
        
        # ИСПРАВЛЕНО: Проверяем, что вернулись на главную, используя метод из BasePage
        assert main_page.get_current_url() == Urls.SAMOKAT_HOME_PAGE

    @allure.title("Проверка клика по логотипу 'Яндекс'")
    @allure.description("При нажатии на логотип Яндекса в новом окне открывается Дзен")
    def test_click_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_yandex_logo()
        
        # ИСПРАВЛЕНО: Вызываем методы переключения и ожидания URL из BasePage
        main_page.switch_to_next_tab()
        
        # Ждем загрузки Dzen.ru
        main_page.check_url_contains(Urls.YANDEX_REDIRECT_URL_PART)
        
        # ИСПРАВЛЕНО: Проверяем URL через метод BasePage
        assert Urls.YANDEX_REDIRECT_URL_PART in main_page.get_current_url()