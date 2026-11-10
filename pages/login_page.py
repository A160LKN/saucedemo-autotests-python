import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.data import BASE_URL


class LoginPage(BasePage):

    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    @allure.step("Открыть страницу входа")
    def open(self):
        self.driver.get(BASE_URL)
        return self

    @allure.step("Войти с логином «{username}» и паролем «{password}»")
    def login(self, username, password):
        self.type_text(self.USERNAME_FIELD, username)
        self.type_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Получить текст ошибки")
    def get_error_text(self):
        return self.wait_for_visible(self.ERROR_MESSAGE).text