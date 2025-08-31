from selenium.webdriver.common.by import By
from .base_page import BasePage


class DashboardPage(BasePage):
    # Locators
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    user_menu = (By.CLASS_NAME, "oxd-userdropdown-tab")   # adjust if different
    logout_button = (By.XPATH, "//a[text()='Logout']")

    def is_loaded(self):
        """Check if dashboard is loaded"""
        return self.is_visible(self.DASHBOARD_HEADER)

    def logout(self):
        """Perform logout"""
        self.click(self.user_menu)
        self.click(self.logout_button)
