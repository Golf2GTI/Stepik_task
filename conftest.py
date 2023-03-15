import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Choose language en/es/ru(etc)')

@pytest.fixture()
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = None
    if user_language == "ar":
        browser = webdriver.Chrome(options=options)
    elif user_language == "ca":
        browser = webdriver.Chrome(options=options)
    elif user_language == "cs":
        browser = webdriver.Chrome(options=options)
    elif user_language == "da":
        browser = webdriver.Chrome(options=options)
    elif user_language == "de":
        browser = webdriver.Chrome(options=options)
    elif user_language == "en-gb":
        browser = webdriver.Chrome(options=options)
    elif user_language == "el":
        browser = webdriver.Chrome(options=options)
    elif user_language == "es":
        browser = webdriver.Chrome(options=options)
    elif user_language == "fi":
        browser = webdriver.Chrome(options=options)
    elif user_language == "fr":
        browser = webdriver.Chrome(options=options)
    elif user_language == "it":
        browser = webdriver.Chrome(options=options)
    elif user_language == "ko":
        browser = webdriver.Chrome(options=options)
    elif user_language == "nl":
        browser = webdriver.Chrome(options=options)
    elif user_language == "pl":
        browser = webdriver.Chrome(options=options)
    elif user_language == "pt":
        browser = webdriver.Chrome(options=options)
    elif user_language == "pt-br":
        browser = webdriver.Chrome(options=options)
    elif user_language == "ro":
        browser = webdriver.Chrome(options=options)
    elif user_language == "ru":
        browser = webdriver.Chrome(options=options)
    elif user_language == "sk":
        browser = webdriver.Chrome(options=options)
    elif user_language == "uk":
        browser = webdriver.Chrome(options=options)
    elif user_language == "zh-hans":
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be not null")
    yield browser
    browser.quit()
