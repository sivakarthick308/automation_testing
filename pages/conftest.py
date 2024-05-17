import configparser

import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def setup_and_tear_down(request):
    browser_name = ""
    url = ""
    try:
        config = configparser.ConfigParser()
        config.read('config.ini', encoding='utf-8')
        browser_name = config.get("browser_info", "browser_name")
        url = config.get("application_info", "url")
    except configparser.NoSectionError:
        raise Exception("No section section in config.ini")

    driver = ""
    if browser_name == "Chrome":
        driver = webdriver.Chrome()
    elif browser_name == "Firefox":
        driver = webdriver.Firefox()
    elif browser_name == "Edge":
        driver = webdriver.Edge()
    else:
        raise Exception("Invalid browser type")

    driver.get(url)
    request.cls.driver = driver
    yield request.cls.driver
    driver.quit()