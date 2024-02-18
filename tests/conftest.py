import pytest
from selenium import webdriver

BROWSERS = {
    'firefox': webdriver.Firefox,
    'chrome': webdriver.Chrome,
}


# инициализация WebDriver, будет выполняться 1 раз за тестовую сессию

@pytest.fixture(scope="session")
def browser():
    for browser in BROWSERS:
        driver = browser
        yield driver
        driver.quit()
