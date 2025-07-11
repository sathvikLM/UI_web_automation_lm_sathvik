import inspect
import logging
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException


# @pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # Ensure Logs directory exists before creating the logfile
        if not logger.handlers:
            logs_dir = './Logs'
            if not os.path.exists(logs_dir):
                os.makedirs(logs_dir)

            fileHandler = logging.FileHandler(f'{logs_dir}/logfile.log')
            formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
            fileHandler.setFormatter(formatter)

            logger.addHandler(fileHandler)
            logger.setLevel(logging.DEBUG)

        return logger

    def ensure_sidebar_expanded(self, side_menu_locator, toggle_button_locator):
    """
    Ensures sidebar is expanded before interacting with menu elements.
    Works around headless/Windows UI issues in Jenkins using JS click + visibility checks.
    """
    log = self.getLogger()
    wait = WebDriverWait(self.driver, 20)

    try:
        log.info("Waiting for sidebar container and toggle button.")
        sidebar = wait.until(EC.presence_of_element_located(side_menu_locator))
        toggle_button = wait.until(EC.presence_of_element_located(toggle_button_locator))

        # If already expanded
        menu_class = sidebar.get_attribute("class")
        log.debug(f"Initial sidebar class: {menu_class}")
        if "mat-drawer-opened" in menu_class:
            log.info("Sidebar already expanded.")
            return

        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", toggle_button)
        time.sleep(1)

        # Ensure it's clickable
        wait.until(EC.element_to_be_clickable(toggle_button_locator))

        # JS click attempt
        log.info("Attempting to expand sidebar using JavaScript click.")
        self.driver.execute_script("arguments[0].click();", toggle_button)

        # Wait for sidebar to open (check class change)
        for i in range(10):
            time.sleep(1)
            menu_class = self.driver.find_element(*side_menu_locator).get_attribute("class")
            log.debug(f"Sidebar class after toggle attempt {i + 1}: {menu_class}")
            if "mat-drawer-opened" in menu_class:
                log.info("Sidebar expanded successfully.")
                return

        # Final fallback: click again
        log.warning("Sidebar not expanded after first click. Retrying JS click...")
        self.driver.execute_script("arguments[0].click();", toggle_button)
        time.sleep(2)
        menu_class = self.driver.find_element(*side_menu_locator).get_attribute("class")
        if "mat-drawer-opened" in menu_class:
            log.info("Sidebar expanded successfully on second attempt.")
            return

        # If still failed
        screenshot_path = "/var/lib/jenkins/workspace/sidebar_failed.png"
        self.driver.save_screenshot(screenshot_path)
        log.error(f"Sidebar failed to expand. Screenshot saved: {screenshot_path}")
        raise TimeoutException("Sidebar did not expand after multiple attempts.")

    except Exception as e:
        log.exception(f"Failed to expand sidebar: {e}")
        raise

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
