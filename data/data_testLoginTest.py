# -*- coding: utf-8 -*-
# Этот класс нжен для облегчения поддержки тестов.
# Все тестовые данные хранятся тут в виде переменных, а в тесты помещается ссылка на переменную этого класса.
# Чтобы сослаться нужно не забыть импотировать класс Data_test_loginTest в класс с тестами.


class DataTestLoginTest:
    # for authorization
    url_login = "https://pro/login"
    url_client = "https://pro/admin/client/search"
    login = "1"
    password = "1"


class DataTestRTList:
    # for Report Template list
    # url_rt_list = "http://1/"
    url_rt_list = "http://2/"
    # url_rt_list = "http://localhost:4000/"
    # url_create_new_rt = "http://3"
    url_create_new_rt = "http://4"
    url_rt_stuffing = ""
    url_rt_view = ""
    TITLE_RT = "RT_created_for_deleting"

    new_rt_name = "Fish and chips"
    description = "Some fish which was fried with potato"


class DataCreateNewRT:
    rt_title = "RT created by autotest"
    rt_title_for_deletion = "RT created by autotest for deletion"
    rt_description = "RT created by autotest description"


class DataEditRT:
    rt_title_edit = "RT created and then edited by autotest"
    rt_description_edit = "RT created and then edited by autotest description"


class DataTestConstructorRT:
    url_constructor_page = "http://5"
    section_title = "Test section #1"
    paragraph_common_text = "Test paragraph #1-2"
    paragraph_for_sub_device_text = "Test paragraph #2-3"
    paragraph_for_additional_device_text = "Test paragraph #2-4"


class DataSections:
    section_title = "Section_1"
    section_title_edited = "Section_1_edited"
