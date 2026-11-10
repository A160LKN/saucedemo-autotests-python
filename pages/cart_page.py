import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):

    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    @allure.step("Получить названия товаров в корзине")
    def get_item_names(self):
        items = self.wait.until(EC.visibility_of_all_elements_located(self.ITEM_NAMES))
        return [item.text for item in items]