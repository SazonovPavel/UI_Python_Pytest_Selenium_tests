# -*- coding: utf-8 -*-
import time

from data.data_testLoginTest import DataTestLoginTest, DataCreateNewRT
from locators.dynamic_locators import created_rt_title_locator
from locators.locators import CreationNevRTPageLocator
from pages_m2.abfp_pages_for_auth.login_page import LoginPageABFP
from pages_m2.rt_pages.rt_list_page import RtListPage


# Этот метод нужен для авторизации и получения странички со списком темплейтов.
def auth_helper(driver):
    LoginPageABFP(driver).correct_log_in(DataTestLoginTest.login, DataTestLoginTest.password)


def create_rt(driver, rt_title):
    rt_list_page = RtListPage(driver)
    creation_rt_page = rt_list_page.button_create_rt()
    creation_rt_page.add_name_to_new_rt(rt_title)
    creation_rt_page.add_description_to_new_rt(DataCreateNewRT.rt_description)
    constructor_page = creation_rt_page.push_btn_start_rt_filling()

    rt_title_control = constructor_page.find_element(created_rt_title_locator(rt_title))
    assert rt_title_control.is_displayed()
    return constructor_page


def create_rt_for_deletion(driver):
    rt_list_page = RtListPage(driver)
    creation_rt_page = rt_list_page.button_create_rt()

    creation_rt_page.add_name_to_new_rt(DataCreateNewRT.rt_title_for_deletion)
    creation_rt_page.add_description_to_new_rt(DataCreateNewRT.rt_description)

    constructor_page = creation_rt_page.push_btn_start_rt_filling()

    rt_title = constructor_page.find_element(CreationNevRTPageLocator.RT_TITLE_FOR_DELETION)
    assert rt_title.is_displayed()
    return constructor_page


def duplicate_draft_rt(driver):
    rt_list_page = RtListPage(driver)
    rt_list_page.draft_order_by_time()

    rt_list_page.call_draft_rt_menu()
    rt_list_page.d_rt_menu_duplicate()
    rt_list_page.d_rt_confirm_duplicate()

    return rt_list_page


def delete_last_created_rt(driver):
    rt_list_page = RtListPage(driver)
    rt_list_page.draft_order_by_time()
    rt_list_page.call_draft_rt_menu()
    rt_list_page.d_rt_menu_delete()
    rt_list_page.d_rt_confirm_delete()
    time.sleep(5)
