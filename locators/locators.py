# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
# вид локатора "(By.XPATH, "локатор")" либо By.*другой тип локатора*


class RtListLocators(object):
    # COMMON ACTION ON THE PAGE
    BTN_CREATE_RT = (By.XPATH, "/html/body/app-root/div/div/div/app-templates/div/div/app-templates-block[1]/div/div/button/span")

    # ORDER BY
    BTN_ORDER_BY_NAME_DRAFT = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/div[1]/div[1]/app-templates[1]/div[1]/div[1]/app-templates-block[1]/div[1]/mat-table[1]/mat-header-row[1]/mat-header-cell[1]/div[1]/button[1]")
    BTN_ORDER_BY_TIME_DRAFT = (By.XPATH, "/html/body/app-root/div/div/div/app-templates/div/div/app-templates-block[1]/div/mat-table/mat-header-row/mat-header-cell[2]/div/button")
    BTN_ORDER_BY_NAME_PUBLISH = (By.XPATH, "")
    BTN_ORDER_BY_NAME_ARCHIVED = (By.XPATH, "")

    # ACTION WITH DRAFT RT
    FIRST_DRAFT_RT = (By.XPATH, "//body//mat-row[1]")
    FIRST_DRAFT_RT_NAME = (By.XPATH, "//mat-row[1]//mat-cell[1]//div[1]//p[1]")
    FIRST_DRAFT_RT_DATA = (By.XPATH, "//mat-row[1]//mat-cell[2]//div[1]")

    SECOND_DRAFT_RT = (By.XPATH, "//body//mat-row[2]")
    SECOND_DRAFT_RT_NAME = (By.XPATH, "//mat-row[2]//mat-cell[1]//div[1]//p[1]")
    SECOND_DRAFT_RT_DATA = (By.XPATH, "//mat-row[2]//mat-cell[2]//div[1]")

    BTN_FIRST_DRAFT_RT_ACTIONS = (By.XPATH, "/html/body/app-root/div/div/div/app-templates/div/div/app-templates-block[1]/div/mat-table/mat-row[1]/mat-cell[4]/app-templates-actions/div/button")
    BTN_DRAFT_RT_EDIT_ACTION = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]")
    BTN_DRAFT_RT_DUPLICATE_ACTION = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[2]")
    BTN_DRAFT_RT_DELETE_ACTION = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[3]")

    # modal window for duplicate rt
    BTN_DUPLICATE_MW_DRAFT_RT = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/mat-dialog-container[1]/app-confirmation-dialog[1]/div[1]/div[2]/button[2]")
    BTN_CANCEL_DUPLICATE_MW_DRAFT_RT = "/html[1]/body[1]/div[1]/div[2]/div[1]/mat-dialog-container[1]/app-confirmation-dialog[1]/div[1]/div[2]/button[1]]"

    # modal window for delete rt
    BTN_DELETE_MW_DRAFT_RT = (By.XPATH, "")
    BTN_CANCEL_DELETE_MW_DRAFT_RT = (By.XPATH, "")

    # ACTION WITH PUBLISH RT
    FIRST_PUBLISH_RT = (By.XPATH, "")

    BTN_FIRST_PUBLISH_RT_ACTIONS = (By.XPATH, "")
    PUBLISH_RT_DUPLICATE_ACTION = (By.XPATH, "//div[@class='mat-menu-content']/button/span[text()=' Duplicate ']")
    PUBLISH_RT_ARCHIVED_ACTION = (By.XPATH, "")

    # modal window for duplicate rt
    BTN_DUPLICATE_MW_PUBLISHED_RT = (By.XPATH, "")
    BTN_CANCEL_DUPLICATE_MW_PUBLISHED_RT = (By.XPATH, "")


    # ACTION WITH ARCHIVED RT
    FIRST_ARCHIVED_RT = (By.XPATH, "")

    FIRST_ARCHIVED_RT_ACTIONS = (By.XPATH, "")
    ARCHIVED_RT_REPUBLISH_ACTION = (By.XPATH, "")
    ARCHIVED_RT_DUPLICATE_ACTION = (By.XPATH, "//div[@class='mat-menu-content']/button/span[text()=' Duplicate ']")

    BTN_DUPLICATE_MW_REPUBLISH_RT = (By.XPATH, "")
    BTN_CANCEL_DUPLICATE_MW_REPUBLISH_RT = (By.XPATH, "")

    # modal window for create rt
    FIELD_NAME_NEW_RT = (By.XPATH, "")
    STR_IN_RT_LIST = (By.XPATH, "")


class ConstructorPageLocators(object):

    # Go to RT list
    BTN_DO_TO_RT_MANAGEMENT_SYSTEM = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-header[1]/div[1]/header[1]/div[1]/div[2]/span[1]")

    # Header DRAFT rt EDIT
    BTN_PUBLISH_RT_DRAFT_EDIT = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-header[1]/div[1]/header[1]/div[2]/div[1]/button[1]")
    BTN_PDF_PREVIEW_DRAFT_EDIT = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-header[1]/div[1]/header[1]/div[2]/div[1]/button[2]")
    BTN_DELETE_DRAFT_EDIT = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-header[1]/div[1]/header[1]/div[2]/div[1]/button[3]")

    # Header DRAFT rt VIEW
    BTN_EDIT_RT_DRAFT_VIEW = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-header[1]/div[1]/header[1]/div[2]/div[1]/button[1]")
    BTN_PUBLISH_RT_DRAFT_VIEW = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-header[1]/div[1]/header[1]/div[2]/div[1]/button[2]")
    BTN_PDF_PREVIEW_DRAFT_VIEW = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-header[1]/div[1]/header[1]/div[2]/div[1]/button[3]")
    BTN_DELETE_DRAFT_VIEW = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-header[1]/div[1]/header[1]/div[2]/div[1]/button[4]")

    # Header PUBLISHED
    BTN_DUPLICATE_RT_PUBLISHED_RT = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-header[1]/div[1]/header[1]/div[2]/div[1]/button[1]")
    BTN_PDF_PREVIEW_PUBLISHED_RT = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-header[1]/div[1]/header[1]/div[2]/div[1]/button[2]")
    BTN_ARCHIVE_PUBLISHED_RT = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-header[1]/div[1]/header[1]/div[2]/div[1]/button[3]")

    # Header ARCHIVED
    BTN_DUPLICATE_ARCHIVED_RT = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-header[1]/div[1]/header[1]/div[2]/div[1]/button[1]")
    BTN_REPUBLISHED_ARCHIVED_RT = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-header[1]/div[1]/header[1]/div[2]/div[1]/button[2]")
    BTN_PDF_PREVIEW_ARCHIVED_RT = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-header[1]/div[1]/header[1]/div[2]/div[1]/button[3]")

    # RT status in Header
    STATUS_RT_HEADER = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-header[1]/div[1]/header[1]/div[2]/div[1]/div[1]/p[1]/span[1]")

    # Modal window for action in Header
    MW_CONFIRM = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/mat-dialog-container[1]/app-confirmation-dialog[1]/div[1]/div[2]/button[2]")
    MW_CANCEL = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/mat-dialog-container[1]/app-confirmation-dialog[1]/div[1]/div[2]/button[1]")

    # RT title, description etc
    TITLE_RT_VIEW = (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/div[1]/div[1]/app-constructor[1]/div[1]/div[1]/div[1]/div[2]/p[1]")

    # Locators for section
    BTN_ADD_SECTION = (By.XPATH, "")
    ADD_SECTION_TITLE = (By.XPATH, "")
    SECTION_BTN_OK = (By.XPATH, "")
    SECTION_BTN_CANCEL = (By.XPATH, "")
    SECTION_DROPDOWN_MENU = (By.XPATH, "")

    # Locators for root paragraph without a link to device
    BTN_ADD_ROOT_PARAGRAPH_NOT_RELATED_TO_DEVICE = (By.XPATH, "")
    ADD_PARAGRAPH_TEXT = (By.XPATH, "")
    BTN_MW_OK_ROOT_PAR_WITHOUT = (By.XPATH, "")
    BTN_MW_CANCEL_ROOT_PAR_WITHOUT = (By.XPATH, "")

    # Locators for root paragraph with a link to device
    BTN_ADD_ROOT_PARAGRAPH_RELATED_TO_DEVICE = (By.XPATH, "")
    ROOT_PARAGRAPH_RELATED_TO_DEVICE_DROPDOWN_SELECT_DEVISE = (By.XPATH, "")
    RELATED_TO_DEVICE_RADIOBUTTON_DEVISE_CARD = (By.XPATH, "")
    RELATED_TO_DEVICE_RADIOBUTTON_CUSTOM_TEXT = (By.XPATH, "")
    BTN_MW_OK_ROOT_PAR_RELATED_TO_DEVICE = (By.XPATH, "")
    BTN_MW_CANCEL_ROOT_PAR_RELATED_TO_DEVICE = (By.XPATH, "")

    # Locators for child paragraph with a sub-device in Report Template Constructor
    BTN_ADD_CHILD_PARAGRAPH_WITH_DEVICE = (By.XPATH, "")
    ADD_SUBDEVICE_RADIOBUTTON_DEVISE_CARD = (By.XPATH, "")
    ADD_SUBDEVICE_RADIOBUTTON_CUSTOM_TEXT = (By.XPATH, "")
    CHILD_PARAGRAPH_FOR_SUB_DEVICE_DROPDOWN_SELECT_DEVISE = (By.XPATH, "")
    BTN_MW_OK_SUB_DEVICE = (By.XPATH, "")
    BTN_MW_CANCEL_SUB_DEVICE = (By.XPATH, "")

    # Locators for child paragraph ‘additional’ Paragraph in Report Template Constructor
    BTN_ADD_CHILD_PARAGRAPH_TO_ADDITIONAL_PARAGRAPH = (By.XPATH, "")
    ADDITIONAL_PARAGRAPH_RADIOBUTTON_DEVICE_CARD = (By.XPATH, "")
    ADDITIONAL_PARAGRAPH_RADIOBUTTON_CUSTOM_TEXT = (By.XPATH, "")
    BTN_MW_OK_ADDITIONAL_PARAGRAPH = (By.XPATH, "")
    BTN_MW_CANCEL_ADDITIONAL_PARAGRAPH = (By.XPATH, "")

    LINK_PARAGRAPH_TO_DEVICE = (By.XPATH, "")
    BTN_ADD_ITEM = (By.XPATH, "")


class CreationNevRTPageLocator(object):
    FIELD_NAME_NEW_RT = (By.XPATH, "/html/body/app-root/div/div/div/app-new-template-page/div/div/mat-card/div/form/mat-form-field[1]/div/div[1]/div/input")
    FIELD_DESCRIPTION_NEW_RT = (By.XPATH, "/html/body/app-root/div/div/div/app-new-template-page/div/div/mat-card/div/form/mat-form-field[2]/div/div[1]/div/input")
    BTN_DISCARD_AND_EXIT = (By.XPATH, "")
    BTN_START_RT_FILLING = (By.XPATH, "/html/body/app-root/div/div/div/app-new-template-page/div/div/div/button[2]")

    # this is dynamic locator
    RT_TITLE_NORMAL = (By.XPATH, "/html/body/app-root/div/div/div/app-constructor/div/div/div[1]/div[2]/p[contains(text(),'RT created by autotest')]")

    RT_TITLE_FOR_DELETION = (By.XPATH, "/html/body/app-root/div/div/div/app-constructor/div/div/div[1]/div[2]/p[contains(text(),'RT created by autotest for deletion')]")

    FIRST_SECTION_POSITION = (By.XPATH, "")
    ROOT_PARAGRAPH_NOT_RELATED_TO_DEVICE = (By.XPATH, "")
    ROOT_PARAGRAPH_RELATED_TO_DEVICE = (By.XPATH, "")
    CHILD_PARAGRAPH_FOR_SUB_DEVICE = (By.XPATH, "")
    CHILD_PARAGRAPH_FOR_ADDITIONAL_DEVICE = (By.XPATH, "")


class ViewRT(object):
    SOME_LOCATOR = (By.XPATH, "")


class DeleteRT(object):
    find_need_rt_by_name = (By.XPATH, "//*[contains(text(),'RT created by autotest for deletion')]")
    BTN_CONFIRM_DELETE_DRAFT_RT = (By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/app-confirmation-dialog/div/div[2]/button[2]")
    ALL_DRAFT_RT_LIST = (By.XPATH, "/html/body/app-root/div/div/div/app-templates/div/div/app-templates-block[1]/div/mat-table/mat-row")


# ADD "(By.XPATH, "локатор")"
class EditRT(object):
    find_need_rt = (By.XPATH, "//*[contains(text(),'RT created by autotest')][1]/../../..//mat-cell[4]/app-template-actions/div/button")
    edit_option = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]")
    btn_active_menu = (By.XPATH, "/html/body/app-root/div/div/div/app-constructor/div/div/div[1]/div[1]/div[2]/button/span/app-template-actions/div/button")
    btn_active_menu_edit = (By.XPATH, "/html/body/div/div[2]/div/div/div/button")
    edit_name_rt = (By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/app-edit-template-dialog/div/div[2]/div/mat-form-field/div/div[1]/div/input")
    edit_description_rt = (By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/app-edit-template-dialog/div/div[3]/div/mat-form-field/div/div[1]/div/input")
    btn_ok_edit_rt = (By.XPATH, "//button[@class='flat-primary-btn mat-raised-button mat-button-base mat-primary']")

    # this is dynamic locator
    rt_title_edited = (By.XPATH, "/html/body/app-root/div/div/div/app-constructor/div/div/div[1]/div[2]/p[contains(text(),'RT created and then edited by autotest')]")


# ADD "(By.XPATH, "локатор")"
class Sections(object):
    add_section_button = (By.XPATH, "/html/body/app-root/div/div/div/app-constructor/div/div/div[3]/button")
    field_section_title = (By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/app-add-section-dialog/div/div[2]/div/mat-form-field/div/div[1]/div/input")
    ok_button = (By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/app-add-section-dialog/div/div[3]/button[2]")
    title_assert = (By.XPATH, "/html/body/app-root/div/div/div/app-constructor/div/div/div[2]/app-section/div/div[2]/p[contains(text(),'Section_1')]")
    active_menu = (By.XPATH, "/html/body/app-root/div/div/div/app-constructor/div/div/div[2]/app-section/div/div[1]/div[2]/button[3]/span/app-section-actions/div/button")
    active_menu_edit = (By.XPATH, "/html/body/div/div[2]/div/div/div/button[1]")
    active_menu_delete = (By.XPATH, "/html/body/div/div[2]/div/div/div/button[2]")
    field_section_title_edited = (By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/app-edit-section-dialog/div/div[2]/div/mat-form-field/div/div[1]/div/input")
    confirmation_edit_button = (By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/app-edit-section-dialog/div/div[3]/button[2]")
    confirmation_delete_button = (By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/app-confirmation-dialog/div/div[2]/button[2]")
    title_edited_assert = (By.XPATH, "/html/body/app-root/div/div/div/app-constructor/div/div/div[2]/app-section/div/div[2]/p[contains(text(),'Section_1_edited')]")
    title_deleted_assert = (By.XPATH, "/html/body/app-root/div/div/div/app-constructor/div/div/div[3]/button/span[contains(text(),'Add section')]")
