# -*- coding: utf-8 -*-
# Такс! НЕ МЕНЯТЬ СТРАНИЦУ! НЕ МЕНЯТЬ НИЧЕГО!!!
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from data.data_testLoginTest import DataTestRTList


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        # test!
        self.base_url = DataTestRTList.url_rt_list

    # Next three method are all basic method. Other action is in Selenium
    def find_element(self, locator, wait=10):
        # return self.driver.find_element_by_xpath(locator)
        return WebDriverWait(self.driver, wait).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, wait=10):
        # return self.driver.find_elements_by_xpath(locator)
        return WebDriverWait(self.driver, wait).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)
