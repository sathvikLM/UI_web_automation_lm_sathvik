from pathlib import Path
from datetime import datetime
import os
import time
import platform
import pytest
import logging
import allure
from slugify import slugify

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# ---------------------------------------------------------------------#
#  1.  Global driver fixture (unchanged except for headless switch)    #
# ---------------------------------------------------------------------#

driver = None

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="function", autouse=True)
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    is_jenkins   = "JENKINS_HOME" in os.environ

    if browser_name == "chrome":
        options = Options()
        if is_jenkins:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
        else:
            options.add_argument("--start-maximized")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        if not is_jenkins:
            driver.set_window_size(1920, 1080)

    elif browser_name == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
    else:
        raise RuntimeError("Unsupported browser")

    driver.get("https://admin.lightmetrics.co/")
    request.cls.driver = driver
    yield
    driver.quit()

# ---------------------------------------------------------------------#
#  2.  Screenshot helper (still used for HTML report)                  #
# ---------------------------------------------------------------------#
def _capture_screenshot(name: str):
    driver.get_screenshot_as_file(name)

# ---------------------------------------------------------------------#
#  3.  Attach screenshot *and log file* to BOTH HTML & Allure          #
# ---------------------------------------------------------------------#
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome     = yield
    report      = outcome.get_result()
    extra       = getattr(report, "extra", [])
    log_file    = max(Path("Logs").glob("run_*.log"), key=lambda p: p.stat().st_mtime)

    # ── attach screenshot on failure ───────────────────────────────────────
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        failed = (report.failed and not xfail) or (report.skipped and xfail)

        if failed:
            scr_dir = Path("Screenshots"); scr_dir.mkdir(exist_ok=True)
            scr_path = scr_dir / f"{slugify(item.nodeid)}.png"
            _capture_screenshot(scr_path)
            # HTML report
            extra.append(pytest_html.extras.png(scr_path))
            # Allure report
            allure.attach.file(
                scr_path,
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
                extension=".png"
            )

    report.extra = extra

    # ── always attach CURRENT log file to Allure for this test ─────────────
    if report.when == "call":
        try:
            with open(log_file, "r", encoding="utf‑8") as f:
                allure.attach(
                    f.read(),
                    name="run log",
                    attachment_type=allure.attachment_type.TEXT
                )
        except Exception as e:
            print(f"[WARN] Could not attach log to Allure: {e}")

# ---------------------------------------------------------------------#
#  4.  HTML report customisation (unchanged)                           #
# ---------------------------------------------------------------------#
def pytest_html_report_title(report):
    report.title = "LightMetrics Technologies Pvt. Ltd"

def pytest_configure(config):
    from platform import python_version
    config._metadata = {
        "tester":            "Sreenivasulu Akki",
        "python_version":    python_version(),
        "manager":           "Divya Gajanana",
        "team":              "QA_Automation",
        "testing_suite":     "Regression Testing",
        "portal":            "Rebranding Portal's",
        "platform":          platform.platform(),
        "run":               datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.append("<h3>TSP : 'Lmpresales'</h3>")
