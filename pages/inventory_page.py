import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.cart_page import CartPage


class InventoryPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Получить заголовок страницы товаров")
    def get_title(self):
        return self.wait_for_visible(self.TITLE).text

    @allure.step("Добавить рюкзак в корзину")
    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BUTTON)

    @allure.step("Удалить рюкзак из корзины")
    def remove_backpack_from_cart(self):
        self.click(self.REMOVE_BACKPACK_BUTTON)

    @allure.step("Получить количество товаров на значке корзины")
    def get_cart_count(self):
        return int(self.wait_for_visible(self.CART_BADGE).text)

    @allure.step("Проверить, что значок корзины скрыт")
    def is_cart_badge_hidden(self):
        return bool(self.wait.until(EC.invisibility_of_element_located(self.CART_BADGE)))

    @allure.step("Открыть корзину")
    def open_cart(self):
        self.click(self.CART_LINK)
        return CartPage(self.driver)