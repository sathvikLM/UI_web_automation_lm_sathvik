from pathlib import Path
from datetime import datetime
import platform
import pytest
import os
import time
from slugify import slugify

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#
# @pytest.fixture(scope="class", autouse=True)
# def setup(request):
#     global driver
#     browser_name = request.config.getoption("browser_name")
#     if browser_name == "chrome":
#         options = Options()
#         # options.add_argument('--headless')
#         options.add_argument('--no-sandbox')
#         options.add_argument('--disable-dev-shm-usage')
#         driver = webdriver.Chrome(service=Service("/home/a/Documents/drivers/chromedriver"))
#     elif browser_name == "firefox":
#         driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
#     elif browser_name == "IE":
#         print("IE driver")
#     driver.get("https://admin.lightmetrics.co/statistics")
#     driver.maximize_window()
#     print(driver.title)
#     request.cls.driver = driver
#     @pytest.mark.usefixtures("setup")
#     class TestYourWebsite:
#         def test_example(self):
#             pass

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--env", action="store", default="QA", help="Environment: QA, BETA or PROD"
    )

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="function", autouse=True)
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    selected_env = request.config.getoption("--env")
    
    if selected_env.upper() == "QA":
        base_url = "https://admin-qa.lightmetrics.co/"
    elif selected_env.upper() == "PROD":
        base_url = "https://admin.lightmetrics.co/"
    elif selected_env.upper() == "BETA":
        base_url = "https://admin-beta.lightmetrics.co/"
    else:
        raise ValueError(f"Unsupported environment: {selected_env}")
        
    is_jenkins = "JENKINS_HOME" in os.environ
    if browser_name == "chrome":
        options = Options()
        if is_jenkins:
         # options.add_argument('--headless')
            options.add_argument("--headless=new")
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
        else:
            options.add_argument("--start-maximized")

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        if not is_jenkins:
            driver.set_window_size(1920, 1080)

        # driver = webdriver.Chrome(service=Service("/home/user/Downloads/chromedriver-linux64/chromedriver"))
        # driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_name == "firefox":
        # driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "IE":
        print("IE driver")
    driver.get(base_url)

    # # ✅ Replacing maximize_window() logic based on headless mode
    # if "--headless" in options.arguments:
    #     driver.set_window_size(1920, 1080)
    # else:
    #     driver.maximize_window()

    print(driver.title)
    request.cls.driver = driver

    def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

    @pytest.fixture()
    def set_up_tear_down_no_login(request) -> None:
        request.set_viewport_size({"width": 1536, "height": 834})
        request.goto("https://admin.lightmetrics.co/")
        yield request

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(item, call):
        pytest_html = item.config.pluginmanager.getplugin("html")
        outcome = yield
        screen_file = ''
        report = outcome.get_result()
        extra = getattr(report, "extra", [])
        if report.when == "call":
            xfail = hasattr(report, "wasxfail")
            if report.failed or xfail and "page" in item.funcargs:
                request = item.funcargs['request']
                screenshot_dir = Path("Screenshots")
                screenshot_dir.mkdir(exist_ok=True)
                screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
                _capture_screenshot(screen_file)

            if (report.skipped and xfail) or (report.failed and not xfail):
                # add the screenshots to the html report
                extra.append(pytest_html.extras.png(screen_file))
            report.extra = extra

# **************** HTML Report ****************** :-

# ########## Changing Title name ############ :-
def pytest_html_report_title(report):
    ''' modifying the title of html report'''
    report.title = "LightMetrics Technologies Pvt. Ltd"

# ############ Changing Environment ############# :-
def pytest_configure(config):
    username = "Sreenivasulu Akki"
    # manager = "Divya"

    # getting python version
    from platform import python_version
    py_version = python_version()
    # overwriting old parameters with new parameters
    config._metadata = {
        "tester": username,
        "python_version": py_version,
        "manager": "Divya Gajanana",
        "team": "QA_Automation",
        "testing_suite": "Regression Testing",
        "portal": "Rebranding Portal's"
    }

# ############## Changing Summary ################ :-
@pytest.mark.optionalhook
# def pytest_html_results_summary(prefix, summary, postfix):
#     ''' modifying the summary in pytest environment'''
#     from py.xml import html
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.append("<h3>TSP : 'Lmpresales'</h3>")
    summary.append("<h3>Summary Placeholder</h3>")
    postfix.append("<h3>Postfix Placeholder</h3>")
