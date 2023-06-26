import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 1440
    browser.config.window_height = 2160
    # driver_options = webdriver.ChromeOptions
    # driver_options.add_argument('--headless')

    yield

    browser.quit()
