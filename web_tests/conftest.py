import os

import pytest
from selene.support.shared import browser

from tests import config
from todomvc_test.model.app import App


@pytest.fixture(scope='function', autouse=True)
# def clear_and_close_browser():
#    yield
#    browser.clear_local_storage()
#    App().close()

def browser_management():
    browser.config.browser_name = \
        os.getenv('browser.config.browser_name', 'chrome')
    browser.config.browser_name = config.options.browser_name

    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager

    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = False
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(),
        options=chrome_options
    )
    browser.config.driver = driver

    yield
    if config.options.browser_quit_after_each_test:
        browser.quit()
    else:
        browser.clear_local_storage()
