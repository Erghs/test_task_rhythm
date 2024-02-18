from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    #В классе BasePage определены базовые методы для работы с WebDriver

    #конструктор, который принимает driver — экземпляр webdriver.
    def __init__(self, driver):
        self.driver = driver
        #base_url, который будет использоваться для открытия страницы.
        self.base_url = 'https://demoqa.com/'

    #ищет элемент и возвращает его
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    #возращает текст, который содержит элемент, переданный в качестве параметра
    def get_text(self, locator):
        element = self.find_element(locator)
        text = ''
        try:
            text = str(element.text)
        except Exception as e:
            print('Error: {0}'.format(e))
        return text

    #переход на указываемую страницу
    def go_to_site(self):
        return self.driver.get(self.base_url)