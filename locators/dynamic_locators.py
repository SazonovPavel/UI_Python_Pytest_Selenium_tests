# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


def created_rt_title_locator(title):
    begin_path = "/html/body/app-root/div/div/div/app-constructor/div/div/div[1]/div[2]/p[contains(text(),'"
    actual_title = title
    end_path = "')]"
    path = begin_path + actual_title + end_path
    rt_title_for_check = (By.XPATH, path)
    return rt_title_for_check


def edited_rt_title_locator(title):
    begin_path = "/html/body/app-root/div/div/div/app-constructor/div/div/div[1]/div[2]/p[contains(text(),'"
    actual_title = title
    end_path = "')]"
    path = begin_path + actual_title + end_path
    rt_title_edited = (By.XPATH, path)
    return rt_title_edited
