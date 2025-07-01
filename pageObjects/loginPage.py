import time

from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "(//input[@id='signInFormUsername'])[2]")
    passwrod = (By.XPATH, "(//input[@id='signInFormPassword'])[2]")
    loginBtn = (By.XPATH, "(//input[@name='signInSubmitButton'])[2]")
    lmpresales = (By.XPATH, "//span[contains(text(),'lmpresales')]/following-sibling::mat-icon")
    customerName = (By.XPATH, "//input[@data-placeholder='Enter customer name']")
    autoComplete = (By.XPATH, "//div[contains(@id,'mat-autocomplete')]")
    customer_tsp_name = (By.XPATH, "//div[contains(@id,'mat-autocomplete')]/mat-option/span")
    applyBtn = (By.XPATH, "//span[text()='Apply']/..")
    mainMenu = (By.XPATH, "//button[@aria-haspopup='menu']")
    masterPortal = (By.XPATH, "//span[text()='Master Portal Login']/..")
    logout = (By.XPATH, "//button[@role='menuitem']/span[text()='Logout']")

    def loginToAdminPage(self):
        self.driver.find_element(*LoginPage.username).send_keys("revathinagaraj93@gmail.com")
        self.driver.find_element(*LoginPage.passwrod).send_keys("Nagarevi@1")
        self.driver.find_element(*LoginPage.loginBtn).click()
        return self.driver.title

    def customer_tsp(self, config):
        time.sleep(5)
        self.driver.find_element(*LoginPage.lmpresales).click()
        self.driver.find_element(*LoginPage.customerName).clear()
        time.sleep(1)
        self.driver.find_element(*LoginPage.customerName).send_keys(config)
        time.sleep(1)
        customre_tsp_name = self.driver.find_element(*LoginPage.customer_tsp_name).text
        self.driver.find_element(*LoginPage.autoComplete).click()
        self.driver.find_element(*LoginPage.applyBtn).click()
        time.sleep(3)
        self.driver.find_element(*LoginPage.mainMenu).click()
        time.sleep(2)
        self.driver.find_element(*LoginPage.masterPortal).click()
        time.sleep(5)
        first_window_Name = self.driver.current_window_handle
        first_window_Name1 = self.driver.window_handles[0]
        second_Window = self.driver.window_handles[1]
        self.driver.switch_to.window(second_Window)
        return self.driver.title