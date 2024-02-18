import os

from selenium.webdriver.remote.webelement import WebElement


class FirstCasePage():

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://demoqa.com/'

        self._web_driver = web_driver
        self.get(url)

    elements_btn = WebElement(id='app')

    chexbox = WebElement(xpath='//*[@id="item-1"]')

    home_toggle = WebElement(xpath='//*[@id="tree-node"]/ol/li/span/button/svg/path')

    downloads_toogle = WebElement(xpath='//*[@id="tree-node"]/ol/li/ol/li[3]/span/button/svg/path')

    rct_checkbox = WebElement(xpath='//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]')
