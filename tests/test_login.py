import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

class TestLogin:
    @pytest.mark.positive
    def test_successful_login(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.enter_username("admin")
        login_page.enter_password("password")
        login_page.click_login()
        
        assert login_page.get_success_message() == "Успешно! Вход выполнен."
    
    @pytest.mark.negative
    def test_wrong_username(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.enter_username("wrong")
        login_page.enter_password("password")
        login_page.click_login()
        
        assert "Ошибка. Неверный логин" in login_page.get_error_message()
    
    @pytest.mark.negative
    def test_wrong_password(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.enter_username("admin")
        login_page.enter_password("wrong")
        login_page.click_login()
        
        assert "Ошибка. Неверный пароль" in login_page.get_error_message()
