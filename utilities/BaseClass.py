import inspect
import logging
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
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

    def ensure_sidebar_expanded(self, side_menu_locator, toggle_button_locator, timeout=15):
        from selenium.common.exceptions import TimeoutException
        wait = WebDriverWait(self.driver, timeout)

        try:
            side_menu = wait.until(EC.presence_of_element_located(side_menu_locator))
            toggle_btn = wait.until(EC.element_to_be_clickable(toggle_button_locator))
            self.scroll_into_view(toggle_btn)

            initial_class = side_menu.get_attribute("class")
            if 'mat-drawer-opened' not in initial_class:
                toggle_btn.click()
                wait.until(lambda d: 'mat-drawer-opened' in side_menu.get_attribute("class"))
        except Exception as e:
            self.log.error(f"Sidebar did not expand after clicking toggle: {e}")
            raise

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
