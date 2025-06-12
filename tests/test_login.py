import pytest
from pages.login_page import LoginPage

VALID_LOGIN = "admin"
VALID_PASSWORD = "password"

class TestLogin:
    @pytest.fixture(scope="function")
    def browser(self):
        from selenium import webdriver
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_successful_login(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
    
        login_page.enter_username(VALID_LOGIN)
        login_page.enter_password(VALID_PASSWORD)
        login_page.click_login_button()
    
        success_message = login_page.get_success_message()
        assert success_message.text == "Успешно! Вход выполнен.", "Сообщение об успешном входе не отображается"

    def test_wrong_login(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
    
        login_page.enter_username("wrong_user")
        login_page.enter_password(VALID_PASSWORD)
        login_page.click_login_button()
    
        error_message = login_page.get_error_message()
        assert error_message.text == "Ошибка: Неверный логин или пароль.", "Сообщение об ошибке не отображается при неправильном логине"

    def test_wrong_password(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
    
        login_page.enter_username(VALID_LOGIN)
        login_page.enter_password("wrong_password")
        login_page.click_login_button()
    
        error_message = login_page.get_error_message()
        assert error_message.text == "Ошибка: Неверный логин или пароль.", "Сообщение об ошибке не отображается при неправильном пароле"
