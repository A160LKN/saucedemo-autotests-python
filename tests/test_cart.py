import allure
import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.data import BACKPACK, PASSWORD, STANDARD_USER


@allure.epic("SauceDemo")
@allure.feature("Корзина")
class TestCart:

    @pytest.fixture(autouse=True)
    def login_as_standard_user(self, driver):
        """Выполняется перед каждым тестом класса: вход на сайт."""
        LoginPage(driver).open().login(STANDARD_USER, PASSWORD)
        self.inventory = InventoryPage(driver)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Товар добавляется в корзину")
    def test_add_product_to_cart(self):
        self.inventory.add_backpack_to_cart()

        assert self.inventory.get_cart_count() == 1

        cart = self.inventory.open_cart()
        assert BACKPACK in cart.get_item_names()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Товар удаляется из корзины")
    def test_remove_product_from_cart(self):
        self.inventory.add_backpack_to_cart()
        self.inventory.remove_backpack_from_cart()

        assert self.inventory.is_cart_badge_hidden()