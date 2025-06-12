from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://berpress.github.io/selenium-login-demo/"
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-btn")
        self.result_div = (By.ID, "result")

    def open(self):
        """Переходит на страницу."""
        self.driver.get(self.url)

    def enter_username(self, username):
        """Вводит логин в поле."""
        username_field = self.driver.find_element(*self.username_input)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        """Вводит пароль в поле."""
        password_field = self.driver.find_element(*self.password_input)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        """Ждёт и кликает на кнопку 'Вход'."""
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_button.click()

    def get_success_message(self):
        """Возвращает элемент сообщения об успехе."""
        success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.result_div)
        )
        return success_message

    def get_error_message(self):
        """Возвращает элемент сообщения об ошибке."""
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.result_div)
        )
        return error_message
