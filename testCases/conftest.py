# conftest.py (Corrected and Final Version)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from pathlib import Path
from slugify import slugify

# This hook adds the --browser_name command-line option to pytest
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Specify browser: chrome or firefox"
    )

# This is the single, authoritative fixture that sets up and tears down the driver.
# It runs once per test class and attaches the driver to the class,
# which makes `self.driver` work in your tests.
@pytest.fixture(scope="class")
def setup(request):
    """
    Sets up a headless, CI-ready WebDriver based on the browser_name.
    Attaches the driver to the test class for use via `self.driver`.
    Handles quitting the driver after all tests in the class are done.
    """
    browser_name = request.config.getoption("browser_name").lower()
    driver = None
    
    print(f"\nINFO: [conftest.py] Setting up '{browser_name}' driver for the test class...")

    # --- Browser Setup ---
    if browser_name == "chrome":
        options = ChromeOptions()
        # CRITICAL: These options are necessary for running in Jenkins/Docker
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        
        # Use webdriver-manager to automatically get the correct driver
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    else:
        raise ValueError(f"Browser '{browser_name}' is not supported. Use 'chrome' or 'firefox'.")

    driver.maximize_window()
    
    # --- Attach driver to the test class ---
    # This is the line that makes `self.driver` work in your tests.
    request.cls.driver = driver
    
    # Yield control to the test class
    yield
    
    # --- Teardown ---
    # This code runs after all tests in the class have finished
    print("\nINFO: [conftest.py] Tearing down driver...")
    driver.quit()


# Hook for taking a screenshot on test failure and adding it to the HTML report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":
        # Check if the test failed and if the class has a driver instance
        if report.failed and hasattr(item.cls, 'driver'):
            driver_instance = item.cls.driver
            
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
            
            print(f"ERROR: Test failed. Capturing screenshot to {screen_file}")
            driver_instance.get_screenshot_as_file(screen_file)
            
            # Add screenshot to the HTML report
            if screen_file:
                html = (f'<div><img src="{screen_file.replace(" ", "%20")}" alt="screenshot" style="width:304px;height:228px;" '
                        f'onclick="window.open(this.src)" align="right"/></div>')
                extra.append(pytest_html.extras.html(html))
    report.extra = extra


# **************** HTML Report Customizations (Preserved from your original file) ******************

def pytest_html_report_title(report):
    ''' modifying the title of html report'''
    report.title = "LightMetrics Technologies Pvt. Ltd"

def pytest_configure(config):
    ''' modifying the environment section of the html report'''
    # getting python version
    from platform import python_version
    py_version = python_version()
    # overwriting old parameters with new parameters
    config._metadata = {
        "tester": "Sreenivasulu Akki",
        "python_version": py_version,
        "manager": "Divya Gajanana",
        "team": "QA_Automation",
        "testing_suite": "Regression Testing",
        "portal": "Rebranding Portal's"
    }

@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    ''' modifying the summary in pytest environment'''
    from py.xml import html
    prefix.extend([html.h3(" TSP : 'Lmpresales' ")])
    summary.extend([html.h3(" ")])
    postfix.extend([html.h3(" ")])
