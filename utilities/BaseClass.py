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


    def ensure_sidebar_expanded(self, side_menu_locator, toggle_button_locator):
        """
            Ensures sidebar is expanded before interacting with menu elements.

            Fix added by Vidya Hampiholi (LightMetrics QA) to address a UI issue where the sidebar
            was collapsed by default on Windows and Jenkins, preventing navigation item interaction.
            """
        log = self.getLogger()
        wait = WebDriverWait(self.driver, 20)

        try:
            log.info("Waiting for sidebar container and toggle button.")
            menu_element = wait.until(EC.presence_of_element_located(side_menu_locator))
            toggle_button = wait.until(EC.element_to_be_clickable(toggle_button_locator))

            menu_class = menu_element.get_attribute("class")
            log.debug(f"Initial sidebar class: {menu_class}")

            if "mat-drawer-opened" not in menu_class:
                log.info("Sidebar collapsed. Expanding it.")
                toggle_button.click()
                time.sleep(1)

                for i in range(10):
                    menu_class = self.driver.find_element(*side_menu_locator).get_attribute("class")
                    if "mat-drawer-opened" in menu_class:
                        log.info("Sidebar expanded successfully.")
                        return
                    time.sleep(1)

                log.error("Sidebar did not expand after clicking toggle.")
                raise TimeoutException("Sidebar did not expand after clicking toggle.")
            else:
                log.info("Sidebar is already expanded.")
        except TimeoutException as e:
            log.error("Timeout while expanding sidebar: " + str(e))
        except NoSuchElementException as e:
            log.error(f"Sidebar or toggle not found: {e}")
        except ElementNotInteractableException as e:
            log.error(f"Toggle button not interactable: {e}")

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
