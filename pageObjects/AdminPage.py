import time
from typing import List

import pytest
from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:

    def __init__(self, driver):
        self.driver = driver

    # username = (By.XPATH, "(//input[@id='signInFormUsername'])[2]")
    username = (By.XPATH, "//input[@name='username']")
    # passwrod = (By.XPATH, "(//input[@id='signInFormPassword'])[2]")
    passwrod = (By.XPATH, "//input[@name='password']")
    # loginBtn = (By.XPATH, "(//input[@name='signInSubmitButton'])[2]")
    loginBtn = (By.XPATH, "//button[@type='submit']")
    lmpresales = (By.XPATH, "//span[contains(text(),'lmpresales')]/following-sibling::mat-icon")
    customerName = (By.XPATH, "//input[@data-placeholder='Enter customer name']")
    autoComplete = (By.XPATH, "//div[contains(@id,'mat-autocomplete')]")
    #customer_tsp_name = (By.XPATH, "//div[contains(@id,'mat-autocomplete')]/mat-option/span")
    customer_tsp_name = (By.XPATH, "//div[contains(@id,'mat-autocomplete')]/mat-option[1]")
    applyBtn = (By.XPATH, "//span[text()='Apply']/..")
    mainMenu = (By.XPATH, "//button[@aria-haspopup='menu']")
    masterPortal = (By.XPATH, "//span[text()='Master Portal Login']/..")
    logout = (By.XPATH, "//div[@role='menu']/div/button[10]")

    def loginToAdminPage(self, log):
        time.sleep(3)
        self.driver.find_element(*AdminPage.username).send_keys("sreenivasulu.akki@lightmetrics.co")
        self.driver.find_element(*AdminPage.passwrod).send_keys("Srinivas@123")
        self.driver.find_element(*AdminPage.loginBtn).click()
        log.info("title of the page :: " + self.driver.title)

        return self.driver.title

    @pytest.mark.skip()
    def customer_tsp(self, log, config):
        time.sleep(5)
        self.driver.find_element(*AdminPage.lmpresales).click()
        self.driver.find_element(*AdminPage.customerName).clear()
        time.sleep(1)
        self.driver.find_element(*AdminPage.customerName).send_keys(config)
        time.sleep(1)
        tsp_names = self.driver.find_element(*AdminPage.customer_tsp_name).text
        # tsp_names =  self.driver.find_elements(*AdminPage.customer_tsp_name)
        # if tsp_names:
        #     tsp_names[0].click()
        #     tsp_texts = [elem.text for elem in tsp_names]
        #     log.info("***************** Admin Customer TSP ******** :: %s", tsp_texts)
        # else:
        #     log.warning("No TSP names found.")
        #
        # return tsp_texts
        log.info("***************** Admin Customre TSP ******** :: " + tsp_names)
        self.driver.find_element(*AdminPage.autoComplete).click()
        self.driver.find_element(*AdminPage.applyBtn).click()
        time.sleep(3)
        self.driver.find_element(*AdminPage.mainMenu).click()
        time.sleep(2)
        self.driver.find_element(*AdminPage.masterPortal).click()
        time.sleep(5)
        first_window_Name = self.driver.current_window_handle
        first_window_Name1 = self.driver.window_handles[0]
        second_Window = self.driver.window_handles[1]
        self.driver.switch_to.window(second_Window)
        return self.driver.title



    def admin_Logout(self):
        time.sleep(5)
        self.driver.find_element(*AdminPage.mainMenu).click()
        time.sleep(5)
        self.driver.find_element(*AdminPage.logout).click()
