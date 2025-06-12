from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://berpress.github.io/selenium-login-demo/"
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.submit_button = (By.ID, "submit")
        self.success_message = (By.XPATH, "//div[contains(text(), 'Успешно! Вход выполнен.')]")
        self.error_message = (By.XPATH, "//div[contains(text(), 'Ошибка входа')]")

    def open(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def submit(self):
        self.driver.find_element(*self.submit_button).click()

    def get_success_message(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.success_message)
        ).text

    def get_error_message(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.error_message)
        ).text
