import pytest
from selenium import webdriver

from test_task_rhythm.pages.DemoQA import DemoQA


#Тест-кейс 1, принимает фикстуру browser
def test_DemoQA(browser):
    page = DemoQA(browser)
    page.go_to_site()
    page.click_on_the_elements_card()
    page.click_on_the_checkbox()
    page.click_on_the_home_toggle()
    page.click_on_the_downloads_toggle()
    page.click_on_the_rct_checkbox()
    assert page.get_text_on_the_display_result_text() == "You have selected :\nwordFile"
