
import pytest
from selene import browser


@pytest.fixture
def open_browser():
    browser.open('https://google.com')


@pytest.fixture
def browser_window(open_browser):
    browser.config.window_width = 1200
    browser.config.window_height = 1080
    yield
    browser.quit()
