from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_visible(self, locator):
        """Дождаться, пока элемент появится, и вернуть его."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Дождаться, пока элемент станет кликабельным, и нажать."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        """Дождаться поля и ввести текст."""
        self.wait_for_visible(locator).send_keys(text)