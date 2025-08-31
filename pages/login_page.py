from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, username, password):
        """Perform login"""
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button)

    def is_loaded(self):
        """Check if login page is loaded"""
        return self.is_visible(self.username_input) and self.is_visible(self.password_input)
