import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента по локатору {locator}")
    def find_element(self, locator, time=10):
        """Ожидает появления элемента в DOM."""
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент не найден: {locator}"
        )

    @allure.step("Клик по элементу {locator}")
    def click_element(self, locator):
        """Кликает по элементу, предварительно прокручивая до него."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Ввод текста '{text}' в поле {locator}")
    def set_text(self, locator, text):
        """Очищает поле и вводит текст."""
        element = self.find_element(locator)
        element.click()
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получение текста из элемента {locator}")
    def get_text(self, locator):
        """Возвращает видимый текст элемента."""
        return self.find_element(locator).text
    
    # --- Методы для работы с драйвером, вынесенные из тестов и Page-классов ---
    
    @allure.step("Проверка, что текущий URL содержит '{url_part}'")
    def check_url_contains(self, url_part, time=10):
        """Ожидает, пока текущий URL не будет содержать заданную часть."""
        WebDriverWait(self.driver, time).until(EC.url_contains(url_part))

    @allure.step("Переключение на новую вкладку")
    def switch_to_next_tab(self):
        """Переключает контекст драйвера на вторую (новую) открытую вкладку."""
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Проверка наличия элемента {locator} без ожидания")
    def check_element_presence(self, locator):
        """
        Проверяет наличие элемента в DOM без явного ожидания (быстро).
        Возвращает список найденных элементов (для проверки наличия куки).
        """
        return self.driver.find_elements(*locator)
    
    @allure.step("Получение текущего URL")
    def get_current_url(self):
        """Возвращает текущий URL страницы."""
        return self.driver.current_url