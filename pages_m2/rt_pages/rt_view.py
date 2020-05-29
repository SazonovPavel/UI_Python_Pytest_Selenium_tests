# -*- coding: utf-8 -*-
# локаторы в классах страниц!
from data.data_testLoginTest import DataTestRTList


class ViewRT:
    # конструктор
    def __init__(self, driver):
        self.driver = driver
        driver.get(DataTestRTList.url_rt_view)
