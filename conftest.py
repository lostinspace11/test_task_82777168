import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="choose browser: chrome or firefox")


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nStarting Chrome browser...")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nStarting Firefox browser...")
        browser = webdriver.Firefox()
    yield browser
    print("\nQuit browser..")
    browser.quit()
