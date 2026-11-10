# SauceDemo Autotests (Python)

Учебный проект UI-автотестов для демо-магазина [saucedemo.com](https://www.saucedemo.com/) на Python.

Этот же проект на Java: [saucedemo-autotests](https://github.com/A160LKN/saucedemo-autotests).

## Стек

- Python 3.10+
- Selenium WebDriver 4
- pytest
- Allure Report

## Что проверяется

**Авторизация**
- успешный вход с верными данными;
- негативные сценарии (параметризованный тест): неверный пароль, заблокированный пользователь, пустой логин, пустой пароль.

**Корзина**
- добавление товара в корзину;
- удаление товара из корзины.

## Особенности проекта

- паттерн **Page Object** с базовым классом `BasePage`;
- **явные ожидания** (`WebDriverWait`) вместо `time.sleep`;
- браузер создаётся и закрывается в **фикстуре** pytest (`conftest.py`);
- **параметризованные тесты** (`@pytest.mark.parametrize`);
- **Allure-отчёт** с шагами (`@allure.step`), разделами (`epic`, `feature`) и важностью тестов (`severity`);
- **скриншот при падении** теста автоматически прикрепляется к отчёту;
- тестовые данные вынесены в отдельный модуль `utils/data.py`.

## Структура

```
├── pages          — Page Object: страницы сайта и действия на них
├── tests          — тесты
├── utils          — тестовые данные
├── conftest.py    — фикстура браузера и скриншот при падении
├── pytest.ini     — настройки pytest
└── requirements.txt
```

## Запуск

Требования: Python 3.10+, Google Chrome, [Allure](https://allurereport.org/) для просмотра отчёта.

```bash
# создать и включить виртуальное окружение
python3 -m venv .venv
source .venv/bin/activate

# установить зависимости
pip install -r requirements.txt

# запустить тесты
pytest

# открыть Allure-отчёт
allure serve allure-results
```