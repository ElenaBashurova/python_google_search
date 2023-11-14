from selene.support.shared import browser
from selene import be, have


def test_google_search(browser_window):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_no_result(browser_window):
    browser.element('[name="q"]').should(be.blank).type('lsidurfjhsdjkfhjk').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))