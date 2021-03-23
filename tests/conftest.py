import pytest
from selene.support.shared import browser

from test_todomvc.model.app import App


@pytest.fixture(scope='function', autouse=True)
def clear_and_close_browser():
    yield
    browser.clear_local_storage()
    App().close()
