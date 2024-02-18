import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



# инициализация WebDriver, будет выполняться 1 раз за тестовую сессию
#Содержит параметры Firefox, chrome для прогода тестов на этих двух браузерах по-очереди
@pytest.fixture(params=["firefox", "chrome"], scope="session")
def browser(request):
    options = Options()
    options.page_load_strategy = 'eager'
    if request.param == "firefox":
        driver = webdriver.Firefox()
    if request.param == "chrome":
        driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
