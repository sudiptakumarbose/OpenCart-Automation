import os.path
from datetime import datetime

import pytest
from selenium import webdriver
import time

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    request.cls.driver = driver
    yield


def pytest_configure(config):
    config._metadata['Project Name'] = 'OpenCart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


@pytest.hookimpl(tryfirst=True, optionalhook=True)
def pytest_configure(config):

    if config.getoption("--html", default=False):
        config.htmlpath = (
            os.path.abspath(os.curdir)+"\\reports\\"
            + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
        )
    yield