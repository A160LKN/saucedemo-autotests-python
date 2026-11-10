import allure
import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.data import LOCKED_OUT_USER, PASSWORD, STANDARD_USER, WRONG_PASSWORD


@allure.epic("SauceDemo")
@allure.feature("Авторизация")
class TestLogin:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Успешный вход с верными данными")
    def test_successful_login(self, driver):
        LoginPage(driver).open().login(STANDARD_USER, PASSWORD)

        inventory = InventoryPage(driver)

        assert inventory.get_title() == "Products"
        assert "inventory.html" in driver.current_url

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Ошибка при входе: {case_name}")
    @pytest.mark.parametrize(
        "case_name, username, password, expected_error",
        [
            ("Неверный пароль", STANDARD_USER, WRONG_PASSWORD, "Username and password do not match"),
            ("Заблокированный пользователь", LOCKED_OUT_USER, PASSWORD, "Sorry, this user has been locked out"),
            ("Пустой логин", "", PASSWORD, "Username is required"),
            ("Пустой пароль", STANDARD_USER, "", "Password is required"),
        ],
        ids=["wrong_password", "locked_out_user", "empty_username", "empty_password"],
    )
    def test_negative_login(self, driver, case_name, username, password, expected_error):
        login_page = LoginPage(driver).open()
        login_page.login(username, password)

        assert expected_error in login_page.get_error_text()