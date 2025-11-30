from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Element not found: {locator}"
        )

    def click_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def set_text(self, locator, text):
        element = self.find_element(locator)
        element.click()
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        return self.find_element(locator).text

    def switch_to_next_tab(self):
        # Переключение на новую вкладку
        self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_for_url_contains(self, url_part):
        WebDriverWait(self.driver, 10).until(EC.url_contains(url_part))