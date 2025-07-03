import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


# @pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # Ensure Logs directory exists before creating the logfile
    logs_dir = './Logs'
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    fileHandler = logging.FileHandler(f'{logs_dir}/logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler) 
    logger.setLevel(logging.DEBUG)
    return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
