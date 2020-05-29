# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
import os


# For CI/CD
# !!!РАСКОМИТИТЬ ПЕРЕД ЗАЛИВОМ В МАСТЕР!!!
# @pytest.yield_fixture()
# def driver(browser):
#     from selenium.webdriver.chrome.options import Options
#     chrome_options = Options()
# #    options.headless = True
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-gpu')
#     driver_init = webdriver.Chrome('/mnt/hdd2/project/tests/chromedriver', options=chrome_options)
#     driver_init.implicitly_wait(10)
#     driver_init.maximize_window()
#     yield driver_init
#     driver_init.quit()


# !!!ЗАКОМИТИТЬ ПЕРЕД ЗАЛИВОМ В МАСТЕР!!!
@pytest.yield_fixture()
def driver(browser):
    driver_init = None
    if os.name == "nt":
        if browser == "chrome":
            driver_init = webdriver.Chrome(executable_path="C:/DATA/tools/chromedriver.exe")
        elif browser == "firefox":
            driver_init = webdriver.Firefox(executable_path="", log_path=os.devnull)
        elif browser == "opera":
            driver_init = webdriver.Opera(executable_path="")
        elif browser == "IE":
            driver_init = webdriver.Opera(executable_path="")

    elif os.name == "Linux":
        if browser == "chrome":
            driver_init = webdriver.Chrome(executable_path="")
        elif browser == "firefox":
            driver_init = webdriver.Firefox(executable_path="", log_path=os.devnull)
        elif browser == "opera":
            driver_init = webdriver.Opera(executable_path="")
        elif browser == "IE":
            driver_init = webdriver.Opera(executable_path="")

    elif os.name == "posix":
        if browser == "chrome":
            driver_init = webdriver.Chrome(executable_path="/Users/a/Documents/webdrivers/"
                                                           "chromedriver/chromedriver")
        elif browser == "firefox":
            driver_init = webdriver.Firefox(executable_path="/Users/a/Documents/webdrivers/"
                                                            "geckodgiver/geckodriver", log_path=os.devnull)
        elif browser == "safari":
            driver_init = webdriver.Safari()
        elif browser == "opera":
            driver_init = webdriver.Opera(executable_path="/Users/a/Documents/webdrivers/"
                                                          "operadriver/operadriver_mac64/operadriver")

    driver_init.implicitly_wait(10)
    driver_init.maximize_window()
    yield driver_init
    driver_init.quit()
