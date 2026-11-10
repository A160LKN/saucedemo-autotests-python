import allure
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """Открывает браузер перед тестом и закрывает после."""
    options = webdriver.ChromeOptions()
    # отключаем всплывающее окно Chrome «смените пароль» после входа
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver  # здесь выполняется тест

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Если тест упал, прикрепляет скриншот к Allure-отчёту."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Скриншот при падении",
                attachment_type=allure.attachment_type.PNG,
            )