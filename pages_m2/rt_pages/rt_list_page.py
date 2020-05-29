# -*- coding: utf-8 -*-

from data.data_testLoginTest import DataTestRTList
from pages_m2.base_page.base_page import BasePage
from locators.locators import RtListLocators, DeleteRT
import time

from pages_m2.rt_pages.rt_constructor_page import ConstructorPage
import pages_m2.rt_pages.creation_rt_page


class RtListPage(BasePage):
    # конструктор
    def __init__(self, driver):
        super().__init__(driver)
        driver.get(DataTestRTList.url_rt_list)

    def button_create_rt(self):
        self.find_element(RtListLocators.BTN_CREATE_RT).click()
        return pages_m2.rt_pages.creation_rt_page.CreateNewRtPage(self.driver)

    def choose_rt_for_looking(self):
        self.driver.find_element_by_xpath(RtListLocators.FIRST_DRAFT_RT).click()

    # button filter by name
    def draft_order_by_name(self):
        self.find_element(RtListLocators.BTN_ORDER_BY_NAME_DRAFT).click()

    # button filter by last edited
    def draft_order_by_time(self):
        self.find_element(RtListLocators.BTN_ORDER_BY_TIME_DRAFT).click()
        time.sleep(1)
        self.find_element(RtListLocators.BTN_ORDER_BY_TIME_DRAFT).click()

    # View some RT.
    def view_last_created_rt(self):
        self.draft_order_by_time()
        self.find_element(RtListLocators.FIRST_DRAFT_RT).click()
        return ConstructorPage(self.driver)

    # DRAFT
    # button call active menu for first draft rt
    def call_draft_rt_menu(self):
        self.find_element(RtListLocators.BTN_FIRST_DRAFT_RT_ACTIONS).click()

    # active menu for draft rt: edit
    def d_rt_menu_edit(self):
        self.find_element(RtListLocators.BTN_DRAFT_RT_EDIT_ACTION).click()

    # active menu for draft rt: duplicate
    def d_rt_menu_duplicate(self):
        time.sleep(2)
        self.find_element(RtListLocators.BTN_DRAFT_RT_DUPLICATE_ACTION).click()

    # active menu for draft rt: delete
    def d_rt_menu_delete(self):
        self.find_element(RtListLocators.BTN_DRAFT_RT_DELETE_ACTION).click()

    # confirmation for delete RT
    def d_rt_confirm_delete(self):
        self.find_element(DeleteRT.BTN_CONFIRM_DELETE_DRAFT_RT).click()

    # PUBLISHED
    # modal window draft duplication: btn duplicate
    def d_rt_confirm_duplicate(self):
        self.find_element(RtListLocators.BTN_DUPLICATE_MW_DRAFT_RT).click()

    # modal window draft duplication: btn cancel
    def d_rt_cancel_duplicate(self):
        self.find_element(RtListLocators.BTN_CANCEL_DUPLICATE_MW_DRAFT_RT).click()

    # button call active menu for first published rt
    def call_published_rt_menu(self):
        self.find_element(RtListLocators.BTN_FIRST_PUBLISH_RT_ACTIONS).click()

    # active menu for published rt: duplicate to draft
    def p_rt_menu_duplicate(self):
        time.sleep(2)
        self.find_element(RtListLocators.PUBLISH_RT_DUPLICATE_ACTION).click()

    # active menu for archive published rt
    def p_tr_menu_archive(self):
        self.find_element(RtListLocators.PUBLISH_RT_ARCHIVED_ACTION)

    # modal window published duplication: btn duplicate
    def p_rt_confirm_duplicate(self):
        self.find_element(RtListLocators.BTN_DUPLICATE_MW_PUBLISHED_RT).click()

    # modal window published duplication: btn cancel
    def p_rt_cancel_duplicate(self):
        self.find_element(RtListLocators.BTN_CANCEL_DUPLICATE_MW_PUBLISHED_RT).click()

    # ARCHIVED
    def archive_published_rt(self):
        return

    def duplicate_archived_to_draft_rt(self):
        return

    def archive_re_published_rt(self):
        return

    def find_rt_in_list_by_title(self):
        return
