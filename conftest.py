from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    print("\n>>> start browser for test")
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\n<<< quit browser..")
    browser.quit()
