import os


from selenium.webdriver.common.by import By

from test_task_rhythm.pages.BasePage import BasePage


class DemoQASearchLocators:
    #Класс для хранения локаторов

    elements_card = (By.CSS_SELECTOR, 'div.card:nth-child(1) > div:nth-child(1) > div:nth-child(1)')

    checkbox = (By.CSS_SELECTOR, '.show > ul:nth-child(1) > li:nth-child(2)')

    home_toggle = (By.XPATH, '//*[@id="tree-node"]/ol/li/span/button')

    downloads_toggle = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/button')

    rct_checkbox =(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]')

    display_result_text = (By.XPATH, '//*[@id="result"]')


class DemoQA(BasePage):

    #Унаследован от BasePage
    # содержит вспомогательные медоды для взаимодействия с локаторами

    def click_on_the_elements_card(self):
        return self.find_element(DemoQASearchLocators.elements_card, time=2).click()

    def click_on_the_checkbox(self):
        return self.find_element(DemoQASearchLocators.checkbox, time=2).click()

    def click_on_the_home_toggle(self):
        return self.find_element(DemoQASearchLocators.home_toggle, time=2).click()

    def click_on_the_downloads_toggle(self):
        return self.find_element(DemoQASearchLocators.downloads_toggle, time=2).click()

    def click_on_the_rct_checkbox(self):
        return self.find_element(DemoQASearchLocators.rct_checkbox, time=2).click()

    def get_text_on_the_display_result_text(self):
        return self.get_text(DemoQASearchLocators.display_result_text)





