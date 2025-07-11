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


    # def ensure_sidebar_expanded(self, side_menu_locator, toggle_button_locator):
    #     """
    #         Ensures sidebar is expanded before interacting with menu elements.

    #         Fix added by Vidya Hampiholi (LightMetrics QA) to address a UI issue where the sidebar
    #         was collapsed by default on Windows and Jenkins, preventing navigation item interaction.
    #         """
    #     log = self.getLogger()
    #     wait = WebDriverWait(self.driver, 20)

    #     try:
    #         log.info("Waiting for sidebar container and toggle button.")
    #         menu_element = wait.until(EC.presence_of_element_located(side_menu_locator))
    #         toggle_button = wait.until(EC.element_to_be_clickable(toggle_button_locator))

    #         menu_class = menu_element.get_attribute("class")
    #         log.debug(f"Initial sidebar class: {menu_class}")

    #         if "mat-drawer-opened" not in menu_class:
    #             log.info("Sidebar collapsed. Expanding it.")
    #             toggle_button.click()
    #             time.sleep(1)

    #             for i in range(10):
    #                 menu_class = self.driver.find_element(*side_menu_locator).get_attribute("class")
    #                 if "mat-drawer-opened" in menu_class:
    #                     log.info("Sidebar expanded successfully.")
    #                     return
    #                 time.sleep(1)

    #             log.error("Sidebar did not expand after clicking toggle.")
    #             raise TimeoutException("Sidebar did not expand after clicking toggle.")
    #         else:
    #             log.info("Sidebar is already expanded.")
    #     except TimeoutException as e:
    #         log.error("Timeout while expanding sidebar: " + str(e))
    #     except NoSuchElementException as e:
    #         log.error(f"Sidebar or toggle not found: {e}")
    #     except ElementNotInteractableException as e:
    #         log.error(f"Toggle button not interactable: {e}")

    def ensure_sidebar_expanded(self, side_menu_locator: tuple, toggle_button_locator: tuple, timeout: int = 20) -> None:
    """
    Expand a collapsed Angular‑Material sidenav in both headed & headless runs.

    • tries ActionChains → native click → JS click, with scroll‑into‑view
    • waits after every attempt for the `mat‑drawer‑opened` class
    • raises a TimeoutException only after every fallback fails
    """

    log  = self.getLogger()
    wait = WebDriverWait(self.driver, timeout)

    # ------------------------------------------------------------------ helpers
    def _is_open() -> bool:
        cls = self.driver.find_element(*side_menu_locator).get_attribute("class")
        return "mat-drawer-opened" in cls

    def _log_state(msg: str) -> None:
        current = self.driver.find_element(*side_menu_locator)\
                             .get_attribute("class")
        log.debug(f"{msg} – current class = {current}")

    # ------------------------------------------------------------------ locate
    log.info("Waiting for sidenav container & toggle button …")
    sidebar = wait.until(EC.presence_of_element_located(side_menu_locator))
    toggle  = wait.until(EC.presence_of_element_located(toggle_button_locator))

    if _is_open():
        log.info("Sidenav already open – nothing to do.")
        return

    # ------------------------------------------------------------------ attempts
    attempts = (
        ("ActionChains click",
         lambda: ActionChains(self.driver)
                 .move_to_element(toggle).pause(.1).click().perform()),

        ("native WebElement.click()", toggle.click),

        ("JavaScript click",
         lambda: self.driver.execute_script("arguments[0].click()", toggle)),
    )

    for name, click_fn in attempts:
        try:
            _log_state(f"Before {name}")
            # always scroll into view first (headless needs it)
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", toggle)
            time.sleep(.3)

            click_fn()                    # perform the click
            wait.until(lambda _: _is_open(), timeout=3)
            log.info(f"Sidenav opened with {name}.")
            return
        except Exception as exc:
            log.warning(f"{name} failed: {exc!r}")
            # small pause before the next variant
            time.sleep(1)

    # ------------------------------------------------------------------ give up
    screenshot = Path("Screenshots") / f"sidenav_fail_{int(time.time())}.png"
    screenshot.parent.mkdir(exist_ok=True)
    self.driver.save_screenshot(str(screenshot))
    log.error(f"Sidenav still closed after all strategies. "
              f"Screenshot saved → {screenshot}")
    raise TimeoutException("Unable to open sidenav – see screenshot & logs.")

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
