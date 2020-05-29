# -*- coding: utf-8 -*-
import pytest
import time

from data.data_testLoginTest import DataTestLoginTest, DataSections
from data.data_testLoginTest import DataCreateNewRT
from pages_m2.abfp_pages_for_auth.login_page import LoginPageABFP
from locators.locators import Sections
from pages_m2.rt_pages.rt_list_page import RtListPage


# Этот метод нужен для авторизации и получения странички со списком темплейтов.
def auth_helper(driver):
    login_page = LoginPageABFP(driver)
    rt_list_page = login_page.correct_log_in(DataTestLoginTest.login, DataTestLoginTest.password)
    return rt_list_page


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("browser", ["chrome"])
def test_create_section(driver, browser):
    # rt_list_page = auth_helper(driver)
    rt_list_page = RtListPage(driver)
    page = rt_list_page.create_section(rt_list_page, DataCreateNewRT.rt_title, DataSections.section_title)
    assert page.check_element_is_displayed(Sections.title_assert)


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("browser", ["chrome"])
def test_edit_section(driver, browser):
    # rt_list_page = auth_helper(driver)
    rt_list_page = RtListPage(driver)
    page = rt_list_page.edit_section(rt_list_page, DataCreateNewRT.rt_title, DataSections.section_title,
                                     DataSections.section_title_edited)
    assert page.check_element_is_displayed(Sections.title_edited_assert)


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("browser", ["chrome"])
def test_delete_section(driver, browser):
    # rt_list_page = auth_helper(driver)
    rt_list_page = RtListPage(driver)
    page = rt_list_page.delete_section(rt_list_page, DataCreateNewRT.rt_title, DataSections.section_title,
                                     DataSections.section_title_edited)
    time.sleep(1)
    assert page.check_element_is_displayed(Sections.title_deleted_assert)

