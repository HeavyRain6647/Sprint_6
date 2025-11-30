import pytest
import allure
from pages.main_page import MainPage
from data import TestData  # Импорт данных

class TestFAQ:
    
    @allure.title("Проверка выпадающего списка в разделе 'Вопросы о важном'")
    @allure.description("Нажимаем на стрелочку вопроса и проверяем, что открылся соответствующий текст ответа.")
    # Используем данные из data.py
    @pytest.mark.parametrize("num, expected_text", TestData.FAQ_DATA)
    def test_faq_questions(self, driver, num, expected_text):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_cookie_accept()
        
        # Скроллим до FAQ и кликаем на нужный вопрос
        main_page.click_faq_question(num)
        
        answer = main_page.get_faq_answer_text(num)
        
        assert answer == expected_text