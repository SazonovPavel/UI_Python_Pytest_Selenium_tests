# -*- coding: utf-8 -*-
# локаторы в классах страниц!
from pages_m2.base_page.base_page import BasePage
from data.data_testLoginTest import DataTestLoginTest
from pages_m2.abfp_pages_for_auth.home_page import ClientPageABFP


# класс страницы
class LoginPageABFP(BasePage):

    LOCATOR_LOGIN_FIELD = "//input[contains(@placeholder,'Enter Email')]"
    LOCATOR_PASS_FIELD = "//input[contains(@placeholder,'Enter Password')]"
    LOCATOR_LOGIN_BUTTON = "//button[text()='LOGIN']"

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(DataTestLoginTest.url_login)

    # методы работы со страницей
    def correct_log_in(self, login, password):
        self.fill_field(login, LoginPageABFP.LOCATOR_LOGIN_FIELD)
        self.fill_field(password, LoginPageABFP.LOCATOR_PASS_FIELD)
        self.push_button(LoginPageABFP.LOCATOR_LOGIN_BUTTON)
        return ClientPageABFP(self.driver)

    def incorrect_log_in(self, login, password):
        self.fill_field(login, LoginPageABFP.LOCATOR_LOGIN_FIELD)
        self.fill_field(password, LoginPageABFP.LOCATOR_PASS_FIELD)
        self.push_button(LoginPageABFP.LOCATOR_LOGIN_BUTTON)
        return self
