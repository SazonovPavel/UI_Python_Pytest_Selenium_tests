# -*- coding: utf-8 -*-
# локаторы в классе страницы
from pages_m2.base_page.base_page import BasePage
from data.data_testLoginTest import DataTestLoginTest

# класс страницы


class ClientPageABFP(BasePage):

    LOGOUT_BY_XPATH = "//a[contains(@class,'app-header__logout-img')]"
    CHECK_USERNAME_BY_XPATH = "//div[contains(@class,'app-header__logout-name')]"

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(DataTestLoginTest.url_client)

    # методы работы со страницей
    def click_logout(self):
        return self.find_element(ClientPageABFP.LOGOUT_BY_XPATH)
