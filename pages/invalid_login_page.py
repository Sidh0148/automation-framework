from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InvalidLoginPage(BasePage):
    # Locators
    ALERT_ERROR = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    REQUIRED_ERROR = (By.XPATH, "//span[contains(@class,'oxd-input-field-error-message')]")

    def get_error_message(self):
        """Return the error message text after invalid/empty login"""
        if self.is_visible(self.ALERT_ERROR):
            return self.get_text(self.ALERT_ERROR)
        elif self.is_visible(self.REQUIRED_ERROR):
            return self.get_text(self.REQUIRED_ERROR)
        return ""

    def is_error_displayed(self):
        """Check if any error message is visible"""
        return self.is_visible(self.ALERT_ERROR) or self.is_visible(self.REQUIRED_ERROR)
