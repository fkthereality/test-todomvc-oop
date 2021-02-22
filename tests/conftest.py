import pytest
from selene.support.shared import browser

from test_todomvc_oop.helpers.app import All


@pytest.fixture(scope='function', autouse=True)
def clear_and_close_browser():
    yield
    browser.clear_local_storage()
    All().close()
