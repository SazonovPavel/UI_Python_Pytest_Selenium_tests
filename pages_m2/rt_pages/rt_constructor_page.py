# -*- coding: utf-8 -*-
from data.data_testLoginTest import *
from locators.locators import *
from selenium.webdriver.support.ui import Select

import pages_m2.rt_pages.rt_list_page
from pages_m2.base_page.base_page import BasePage


# класс страницы
class ConstructorPage(BasePage):
    # конструктор
    def __init__(self, driver):
        super().__init__(driver)
    # ВАЖНО! Не добавлять driver.get(... итд!!! Тут должен использоваться current_url из самого driver

    def back_to_rt_list(self):
        self.find_element(ConstructorPageLocators.BTN_DO_TO_RT_MANAGEMENT_SYSTEM)
        return pages_m2.rt_pages.rt_list_page.RtListPage(self.driver)

    # методы переписывать вызывая методы BasePage!
    def create_section(self, rt_list_page, title_rt, title_section):
        rt_list_page.find_elment(RtListLocators.BTN_CREATE_RT).click()
        rt_list_page.find_elment(CreationNevRTPageLocator.FIELD_NAME_NEW_RT).send_keys(title_rt)
        rt_list_page.find_elment(CreationNevRTPageLocator.FIELD_DESCRIPTION_NEW_RT).\
            send_keys(DataCreateNewRT.rt_description)
        rt_list_page.find_elment(CreationNevRTPageLocator.BTN_START_RT_FILLING).click()
        rt_list_page.find_elment(Sections.add_section_button).click()
        rt_list_page.find_elment(title_section, Sections.field_section_title)
        rt_list_page.find_elment(Sections.ok_button).click()
        return self

    def edit_section(self, rt_list_page, title_rt, title_section, title_section_edited):
        rt_list_page.create_section(title_rt, title_section)
        rt_list_page.find_elment(Sections.active_menu).click()
        rt_list_page.find_elment(Sections.active_menu_edit).click()
        rt_list_page.find_elment(Sections.field_section_title_edited).send_keys(title_section_edited)
        rt_list_page.find_elment(Sections.confirmation_edit_button).click()
        return self

    def delete_section(self, rt_list_page, title_rt, title_section):
        rt_list_page.create_section(title_rt, title_section)
        rt_list_page.find_elment(Sections.active_menu).click()
        rt_list_page.find_elment(Sections.active_menu_delete).click()
        rt_list_page.find_elment(Sections.confirmation_delete_button).click()
        return self

    def create_root_paragraph_not_related_to_any_device(self):
        self.driver.find_element(ConstructorPageLocators.BTN_ADD_ROOT_PARAGRAPH_NOT_RELATED_TO_DEVICE).click()
        self.driver.find_element(ConstructorPageLocators.ADD_PARAGRAPH_TEXT).clear()
        self.driver.find_element(ConstructorPageLocators.ADD_PARAGRAPH_TEXT) \
            .send_keys(DataTestConstructorRT.paragraph_common_text)
        self.driver.find_element(ConstructorPageLocators.BTN_MW_OK_ROOT_PAR_WITHOUT).click()

    def create_root_paragraph_for_another_device(self):
        self.driver.find_element(ConstructorPageLocators.BTN_ADD_ROOT_PARAGRAPH_RELATED_TO_DEVICE).click()
        select_devise = Select(self.driver.find_element(
            ConstructorPageLocators.ROOT_PARAGRAPH_RELATED_TO_DEVICE_DROPDOWN_SELECT_DEVISE))
        select_devise.select_by_visible_text("NAC Panel")
        self.driver.find_element(ConstructorPageLocators.RELATED_TO_DEVICE_RADIOBUTTON_DEVISE_CARD)
        self.driver.find_element(ConstructorPageLocators.BTN_MW_OK_ROOT_PAR_RELATED_TO_DEVICE).click()

    def create_child_paragraph_for_sub_device(self):
        self.driver.find_element(ConstructorPageLocators.BTN_ADD_CHILD_PARAGRAPH_WITH_DEVICE).click()
        select_device = Select(self.driver.find_element_by_xpath(
            ConstructorPageLocators.CHILD_PARAGRAPH_FOR_SUB_DEVICE_DROPDOWN_SELECT_DEVISE))
        select_device.select_by_visible_text("NAC Panel")
        self.driver.find_element(ConstructorPageLocators.ADD_SUBDEVICE_RADIOBUTTON_CUSTOM_TEXT) \
            .send_keys(DataTestConstructorRT.paragraph_for_sub_device_text)
        self.driver.find_element(ConstructorPageLocators.BTN_MW_OK_SUB_DEVICE).click()

    def create_new_child_paragraph_to_additional_device(self):
        self.driver.find_element(ConstructorPageLocators.
                                 BTN_ADD_CHILD_PARAGRAPH_TO_ADDITIONAL_PARAGRAPH).click()
        self.driver.find_element(ConstructorPageLocators.ADDITIONAL_PARAGRAPH_RADIOBUTTON_CUSTOM_TEXT) \
            .send_keys(DataTestConstructorRT.paragraph_for_additional_device_text)
        self.driver.find_element(ConstructorPageLocators.BTN_MW_OK_ADDITIONAL_PARAGRAPH)

    def create_new_item(self):
        self.driver.find_element(ConstructorPageLocators.BTN_ADD_ITEM).click()


# Edit RT Page

    def edit_rt_active_menu(self):
        self.find_element(EditRT.btn_active_menu).click()

    def active_menu_option_edit(self):
        self.find_element(EditRT.btn_active_menu_edit).click()

    def add_name_to_edit_rt(self, new_rt_name):
        element = self.find_element(EditRT.edit_name_rt)
        element.clear()
        element.send_keys(new_rt_name)

    def add_description_to_edit_rt(self, description):
        element = self.find_element(EditRT.edit_description_rt)
        element.clear()
        element.send_keys(description)

    def push_btn_ok_edit_rt(self):
        self.find_element(EditRT.btn_ok_edit_rt).click()
