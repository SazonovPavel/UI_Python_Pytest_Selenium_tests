# -*- coding: utf-8 -*-
# локаторы в классах страниц!
from data.data_testLoginTest import DataTestRTList


# класс страницы
from pages_m2.base_page.base_page import BasePage
from locators.locators import *
from pages_m2.rt_pages.rt_constructor_page import ConstructorPage


class CreateNewRtPage(BasePage):
    # конструктор
    def __init__(self, driver):
        super().__init__(driver)
        driver.get(DataTestRTList.url_create_new_rt)

    def add_name_to_new_rt(self, new_rt_name):
        element = self.find_element(CreationNevRTPageLocator.FIELD_NAME_NEW_RT)
        element.clear()
        element.send_keys(new_rt_name)

    def add_description_to_new_rt(self, description):
        element = self.find_element(CreationNevRTPageLocator.FIELD_DESCRIPTION_NEW_RT)
        element.clear()
        element.send_keys(description)

    def push_btn_start_rt_filling(self):
        self.find_element(CreationNevRTPageLocator.BTN_START_RT_FILLING).click()
        return ConstructorPage(self.driver)

    def exit_without_creation_rt(self):
        self.driver.find_element(CreationNevRTPageLocator.BTN_DISCARD_AND_EXIT).click()

