import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.invalid_login_page import InvalidLoginPage
from utils.config import config


@pytest.mark.parametrize("username,password,expected,expected_error", [
    # Valid case
    (config.get("valid_user")["username"], config.get("valid_user")["password"], True, None),

    # Invalid credentials
    (config.get("invalid_user")["username"], config.get("invalid_user")["password"], False, "Invalid credentials"),

    # Empty fields
    ("", "", False, "Required"),
])
def test_login(browser, username, password, expected, expected_error):
    """
    Parametrized login test for valid, invalid and empty credentials
    """
    login = LoginPage(browser)
    login.login(username, password)

    if expected:
        dashboard = DashboardPage(browser)
        assert dashboard.is_loaded(), "Dashboard did not load for valid login"
    else:
        invalid_page = InvalidLoginPage(browser)
        error_message = invalid_page.get_error_message()
        assert expected_error in error_message, f"Expected '{expected_error}' but got '{error_message}'"


def test_valid_login(browser):
    """
    Explicit valid login test
    """
    login = LoginPage(browser)
    login.login(config.get("valid_user")["username"], config.get("valid_user")["password"])

    dashboard = DashboardPage(browser)
    assert dashboard.is_loaded(), "Dashboard did not load after valid login"


def test_invalid_login(browser):
    """
    Explicit invalid login test
    """
    login = LoginPage(browser)
    login.login(config.get("invalid_user")["username"], config.get("invalid_user")["password"])

    invalid_page = InvalidLoginPage(browser)
    error_message = invalid_page.get_error_message()
    assert "Invalid credentials" in error_message, f"Unexpected error message: {error_message}"
