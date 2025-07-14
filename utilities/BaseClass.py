import inspect
import logging
import os
import time
from pathlib import Path                               # NEW
from selenium.webdriver.common.action_chains import ActionChains  # NEW

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementNotInteractableException,
)


# @pytest.mark.usefixtures("setup")
class BaseClass:
    # ------------------------------------------------------------------ logger
    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        if not logger.handlers:  # create file‑handler only once
            logs_dir = "./Logs"
            os.makedirs(logs_dir, exist_ok=True)

            file_handler = logging.FileHandler(f"{logs_dir}/logfile.log")
            formatter = logging.Formatter(
                "%(asctime)s :%(levelname)s : %(name)s :%(message)s"
            )
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.setLevel(logging.DEBUG)

        return logger

    # ---------------------------------------------------------------- sidebar
    def ensure_sidebar_expanded(
        self,
        side_menu_locator: tuple,
        toggle_button_locator: tuple,
        timeout: int = 20,
    ) -> None:
        """
        Expand a collapsed Angular‑Material sidenav both locally and on Jenkins.

        • tries ActionChains → native click → JS click, with scroll‑into‑view  
        • waits after every attempt for the `mat‑drawer‑opened` class  
        • makes a screenshot and raises after all attempts fail
        """
        log = self.getLogger()
        wait = WebDriverWait(self.driver, timeout)

        # ---------- helper ---------------------------------------------------
        def _is_open() -> bool:
            cls = self.driver.find_element(*side_menu_locator).get_attribute("class")
            return "mat-drawer-opened" in cls

        # ---------- locate elements -----------------------------------------
        log.info("Waiting for sidenav container & toggle button …")
        sidebar = wait.until(EC.presence_of_element_located(side_menu_locator))
        toggle = wait.until(EC.element_to_be_clickable(toggle_button_locator))

        if _is_open():
            log.info("Sidenav already open – nothing to do.")
            return

        # ---------- attempt list --------------------------------------------
        attempts = (
            (
                "ActionChains click",
                lambda: ActionChains(self.driver)
                .move_to_element(toggle)
                .pause(0.1)
                .click()
                .perform(),
            ),
            ("native WebElement.click()", toggle.click),
            (
                "JavaScript click",
                lambda: self.driver.execute_script("arguments[0].click()", toggle),
            ),
        )

        for name, click_fn in attempts:
            try:
                # always scroll into view first (important in headless)
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", toggle
                )
                time.sleep(0.3)

                click_fn()  # perform the click
                wait.until(lambda _: _is_open(), timeout=3)
                log.info(f"Sidenav opened with {name}.")
                return
            except Exception as exc:
                log.warning(f"{name} failed: {exc!r}")
                time.sleep(1)  # short pause before next method

        # ---------- give up --------------------------------------------------
        screenshot = Path("Screenshots") / f"sidenav_fail_{int(time.time())}.png"
        screenshot.parent.mkdir(exist_ok=True)
        self.driver.save_screenshot(str(screenshot))
        log.error(
            f"Sidenav still closed after all strategies. "
            f"Screenshot saved → {screenshot}"
        )
        raise TimeoutException("Unable to open sidenav – see screenshot & logs.")

    # ---------------------------------------------------------------- misc
    def verifyLinkPresence(self, text):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )

    def selectOptionByText(self, locator, text):
        Select(locator).select_by_visible_text(text)
