import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("admin")
    login_page.enter_password("password")
    login_page.submit()
    assert login_page.get_success_message() == "Успешно! Вход выполнен."

def test_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("wrong_user")
    login_page.enter_password("password")
    login_page.submit()
    assert "Ошибка входа" in login_page.get_error_message()

def test_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("admin")
    login_page.enter_password("wrong_pass")
    login_page.submit()
    assert "Ошибка входа" in login_page.get_error_message()
