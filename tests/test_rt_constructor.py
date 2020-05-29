# -*- coding: utf-8 -*-
import pytest

from additional_logic_level.helpers_rt.helpers_rt import *
from data.data_testLoginTest import *
from data.data_dynamic import *
from locators.locators import *
from locators.dynamic_locators import *

import time


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("browser", ["chrome"])
def test_create_rt(driver, browser):
    # auth_helper(driver)
    rt_title = get_new_rt_title()
    constructor_rt_page = create_rt(driver, rt_title)
    rt_title_control = constructor_rt_page.find_element(created_rt_title_locator(rt_title)).text
    assert rt_title_control == rt_title.upper()

    delete_last_created_rt(driver)


# in progress
@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("browser", ["chrome"])
def test_edit_draft_rt(driver, browser):
    # auth_helper(driver)
    rt_title = get_new_rt_title()
    constructor_rt_page = create_rt(driver, rt_title)

    updated_rt_title = get_updated_rt_title(rt_title)

    constructor_rt_page.edit_rt_active_menu()
    constructor_rt_page.active_menu_option_edit()
    constructor_rt_page.add_name_to_edit_rt(updated_rt_title)
    constructor_rt_page.add_description_to_edit_rt(DataEditRT.rt_description_edit)
    constructor_rt_page.push_btn_ok_edit_rt()

    edited_rt_title = constructor_rt_page.find_element(edited_rt_title_locator(updated_rt_title))
    assert edited_rt_title.is_displayed()
    assert edited_rt_title.text == updated_rt_title.upper()

    delete_last_created_rt(driver)


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("browser", ["chrome"])
def test_duplicate_draft_rt_from_active_menu(driver, browser):
    # auth_helper(driver)
    rt_title = get_new_rt_title()
    create_rt(driver, rt_title)

    rt_list_page = duplicate_draft_rt(driver)
    time.sleep(2)
    first_rt_name = rt_list_page.find_element(RtListLocators.FIRST_DRAFT_RT_NAME).text
    second_rt_name = rt_list_page.find_element(RtListLocators.SECOND_DRAFT_RT_NAME).text

    assert first_rt_name == second_rt_name

    delete_last_created_rt(driver)
    delete_last_created_rt(driver)


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("browser", ["chrome"])
def test_delete_draft_rt(driver, browser):
    # auth_helper(driver)
    constructor_page = create_rt_for_deletion(driver)
    rt_list_page = constructor_page.back_to_rt_list()

    number_before = len(rt_list_page.find_elements(DeleteRT.ALL_DRAFT_RT_LIST))

    rt_list_page.draft_order_by_time()
    rt_list_page.call_draft_rt_menu()
    rt_list_page.d_rt_menu_delete()
    rt_list_page.d_rt_confirm_delete()
    time.sleep(5)

    number_after = len(rt_list_page.find_elements(DeleteRT.ALL_DRAFT_RT_LIST))
    assert number_after == (number_before - 1)


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("browser", ["chrome"])
def test_duplicate_published_rt(driver, browser):
    # auth_helper(driver)
    rt_title = get_new_rt_title()
    constructor_rt_page = create_rt(driver, rt_title)

    constructor_rt_page.find_element(ConstructorPageLocators.BTN_PUBLISH_RT_DRAFT_EDIT).click()
    time.sleep(2)
    constructor_rt_page.find_element(ConstructorPageLocators.MW_CONFIRM).click()
    time.sleep(2)

    constructor_rt_page.find_element(ConstructorPageLocators.BTN_DUPLICATE_RT_PUBLISHED_RT).click()
    time.sleep(2)
    constructor_rt_page.find_element(ConstructorPageLocators.MW_CONFIRM).click()
    time.sleep(2)

    status_rt = constructor_rt_page.find_element(ConstructorPageLocators.STATUS_RT_HEADER)

    assert status_rt.text == "Draft", "Can't duplicate published RT!"
    delete_last_created_rt(driver)


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("browser", ["chrome"])
def test_duplicate_archived_rt(driver, browser):
    # auth_helper(driver)
    rt_title = get_new_rt_title()
    constructor_rt_page = create_rt(driver, rt_title)

    constructor_rt_page.find_element(ConstructorPageLocators.BTN_PUBLISH_RT_DRAFT_EDIT).click()
    time.sleep(2)
    constructor_rt_page.find_element(ConstructorPageLocators.MW_CONFIRM).click()
    time.sleep(2)

    constructor_rt_page.find_element(ConstructorPageLocators.BTN_ARCHIVE_PUBLISHED_RT).click()
    time.sleep(2)
    constructor_rt_page.find_element(ConstructorPageLocators.MW_CONFIRM).click()
    time.sleep(2)

    constructor_rt_page.find_element(ConstructorPageLocators.BTN_DUPLICATE_ARCHIVED_RT).click()
    time.sleep(2)
    constructor_rt_page.find_element(ConstructorPageLocators.MW_CONFIRM).click()
    time.sleep(2)
    status_rt = constructor_rt_page.find_element(ConstructorPageLocators.STATUS_RT_HEADER)

    assert status_rt.text == "Draft", "Can't duplicate archived RT!"
    delete_last_created_rt(driver)


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("browser", ["chrome"])
def test_status_draft_to_published_rt(driver, browser):
    rt_title = get_new_rt_title()
    constructor_rt_page = create_rt(driver, rt_title)

    constructor_rt_page.find_element(ConstructorPageLocators.BTN_PUBLISH_RT_DRAFT_EDIT).click()
    time.sleep(2)
    constructor_rt_page.find_element(ConstructorPageLocators.MW_CONFIRM).click()
    time.sleep(2)

    status_rt = constructor_rt_page.find_element(ConstructorPageLocators.STATUS_RT_HEADER)
    assert status_rt.text == "Published", "Can't publish draft RT!"


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("browser", ["chrome"])
def test_status_draft_to_deleted_rt_header(driver, browser):
    rt_title = get_new_rt_title()
    constructor_rt_page = create_rt(driver, rt_title)
    rt_list_page = constructor_rt_page.back_to_rt_list()

    number_before = len(rt_list_page.find_elements(DeleteRT.ALL_DRAFT_RT_LIST))

    constructor_rt_page = rt_list_page.view_last_created_rt()

    constructor_rt_page.find_element(ConstructorPageLocators.BTN_DELETE_DRAFT_VIEW).click()
    time.sleep(2)
    constructor_rt_page.find_element(ConstructorPageLocators.MW_CONFIRM).click()
    time.sleep(2)

    number_after = len(rt_list_page.find_elements(DeleteRT.ALL_DRAFT_RT_LIST))
    assert number_after == (number_before - 1)
    delete_last_created_rt(driver)


# Это Republish
@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("browser", ["chrome"])
def test_status_archived_to_published_rt(driver, browser):
    rt_title = get_new_rt_title()
    constructor_rt_page = create_rt(driver, rt_title)

    constructor_rt_page.find_element(ConstructorPageLocators.BTN_PUBLISH_RT_DRAFT_EDIT).click()
    time.sleep(2)
    constructor_rt_page.find_element(ConstructorPageLocators.MW_CONFIRM).click()
    time.sleep(2)

    constructor_rt_page.find_element(ConstructorPageLocators.BTN_ARCHIVE_PUBLISHED_RT).click()
    time.sleep(2)
    constructor_rt_page.find_element(ConstructorPageLocators.MW_CONFIRM).click()
    time.sleep(2)

    constructor_rt_page.find_element(ConstructorPageLocators.BTN_REPUBLISHED_ARCHIVED_RT).click()
    time.sleep(2)
    constructor_rt_page.find_element(ConstructorPageLocators.MW_CONFIRM).click()
    time.sleep(2)

    status_rt = constructor_rt_page.find_element(ConstructorPageLocators.STATUS_RT_HEADER)
    assert status_rt.text == "Published", "Can't republish draft RT!"


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("browser", ["chrome"])
def test_status_published_to_archived_rt(driver, browser):
    rt_title = get_new_rt_title()
    constructor_rt_page = create_rt(driver, rt_title)

    constructor_rt_page.find_element(ConstructorPageLocators.BTN_PUBLISH_RT_DRAFT_EDIT).click()
    time.sleep(2)
    constructor_rt_page.find_element(ConstructorPageLocators.MW_CONFIRM).click()
    time.sleep(2)

    constructor_rt_page.find_element(ConstructorPageLocators.BTN_ARCHIVE_PUBLISHED_RT).click()
    time.sleep(2)
    constructor_rt_page.find_element(ConstructorPageLocators.MW_CONFIRM).click()
    time.sleep(2)

    status_rt = constructor_rt_page.find_element(ConstructorPageLocators.STATUS_RT_HEADER)
    assert status_rt.text == "Archived", "Can't archive published RT!"


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("browser", ["chrome"])
def test_read_rt(driver, browser):
    rt_title = get_new_rt_title()
    constructor_rt_page = create_rt(driver, rt_title)
    rt_list_page = constructor_rt_page.back_to_rt_list()
    constructor_rt_page = rt_list_page.view_last_created_rt()
    control_title = constructor_rt_page.find_element(ConstructorPageLocators.TITLE_RT_VIEW).text

    assert control_title == rt_title.upper()
    delete_last_created_rt(driver)

# python3 -m pytest --setup-show tests/test_rt_constructor.py
