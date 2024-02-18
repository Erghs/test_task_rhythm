import pytest
from selenium import webdriver

from test_task_rhythm.pages.DemoQA import DemoQA

class test_DemoQA:

    browser_chrome = webdriver.Chrome()
    browser_firefox = webdriver.Firefox()

    @pytest.mark.parametrize(
        "webdriver",
        [browser_chrome, browser_firefox]
    )
    def test_case_1(self, web_driver):
        page = DemoQA(web_driver)
        page.go_to_site()
        page.click_on_the_elements_card()
        page.click_on_the_home_toggle()
        page.click_on_the_checkbox()
        page.click_on_the_downloads_toggle()
        page.click_on_the_rct_checkbox()
        page.get_text_on_the_display_result_text()

        assert page.get_text_on_the_display_result_text() == "You have selected : wordFile"

