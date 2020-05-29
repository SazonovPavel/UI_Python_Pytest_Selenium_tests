import pytest

from pages_m2.abfp_pages_for_auth.home_page import ClientPageABFP
from pages_m2.abfp_pages_for_auth.login_page import LoginPageABFP
from data.data_testLoginTest import DataTestLoginTest


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("browser", ["chrome"])
def test_correct_auth_test(driver, browser):
    client_page = LoginPageABFP(driver).correct_log_in(DataTestLoginTest.login, DataTestLoginTest.password)
    assert client_page.check_element_is_displayed(ClientPageABFP.CHECK_USERNAME_BY_XPATH)


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("browser", ["chrome", "firefox", "opera", "safari"])
@pytest.mark.parametrize("login", ["", "Wrong Login"])
@pytest.mark.parametrize("password", ["", "Wrong Password"])
def test_incorrect_auth_test(driver, browser, login, password):
    login_page = LoginPageABFP(driver).incorrect_log_in(login, password)
    assert login_page.check_element_is_displayed(LoginPageABFP.LOCATOR_LOGIN_FIELD)
