import pytest
import os
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.config import config


def pytest_addoption(parser):
    """Add CLI options for pytest"""
    parser.addoption("--browser", action="store", default=None, help="Browser: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")


@pytest.fixture
def browser(request):
    """Fixture to initialize browser based on config + CLI options"""

    # Priority: CLI > config.json
    browser_name = request.config.getoption("--browser") or config.get("browser", "chrome")
    headless = request.config.getoption("--headless") or config.get("headless", False)
    timeout = config.get("timeout", 10)

    if browser_name.lower() == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")   # Chrome 109+ syntax
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    elif browser_name.lower() == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Browser {browser_name} not supported")

    driver.maximize_window()
    driver.implicitly_wait(timeout)

    # Navigate to base URL
    base_url = config.get("base_url")
    if base_url:
        driver.get(base_url)

    yield driver
    driver.quit()
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            # Create screenshots folder if not exists
            screenshots_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            # Save screenshot with timestamp + test name
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)
            print(f"\n Screenshot saved to {file_path}")