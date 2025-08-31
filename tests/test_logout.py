from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import config


def test_logout(browser):
    """
    Test that user can log out successfully
    """
    # Step 1: Login
    login = LoginPage(browser)
    login.login(config.get("valid_user")["username"], config.get("valid_user")["password"])

    dashboard = DashboardPage(browser)
    assert dashboard.is_loaded(), "Dashboard did not load after login"

    # Step 2: Logout
    dashboard.logout()

    # Step 3: Verify redirect back to login page
    new_login = LoginPage(browser)
    assert new_login.is_loaded(), "Login page did not load after logout"
    assert "login" in browser.current_url.lower(), "Did not return to login page after logout"
