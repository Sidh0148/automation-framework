from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        """Navigate to a given URL"""
        self.driver.get(url)

    def find(self, locator):
        """Wait for element and return it"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element {locator} not found within timeout")

    def click(self, locator):
        """Click an element"""
        element = self.find(locator)
        element.click()

    def type(self, locator, text):
        """Clear and type text into input"""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get element text"""
        element = self.find(locator)
        return element.text

    def is_visible(self, locator):
        """Check if element is visible on the page"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
