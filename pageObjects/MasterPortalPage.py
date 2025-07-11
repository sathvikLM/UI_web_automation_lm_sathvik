import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass



class MasterPortalPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        super().__init__()


    # feature_announce_btn = (By.XPATH, "//h3[text()='Feature Announcement']/parent::div")
    # closebtn = (By.XPATH, "//h3[text()='Feature Announcement']/parent::div/following-sibling::button")
    feature_announce_btn = (By.XPATH, "//app-feature-announcement[@class='ng-star-inserted']/div/div/div")
    closebtn = (By.XPATH, "//app-feature-announcement[@class='ng-star-inserted']/div/div/div/following-sibling::button")
    toolbar_menu = (By.XPATH, "//app-home[@class='ng-star-inserted']//app-header/mat-toolbar/div[2]/span")
    toolbar_menu_fleet = (By.XPATH, "//mat-toolbar[@class='mat-toolbar header mat-toolbar-single-row ng-star-inserted']/div[2]/div/h3")
    #version_number = (By.XPATH, "//mat-toolbar[@fxlayoutalign='space-between center']/div/mat-chip-list/div/mat-chip")
    version_number = (By.XPATH, "//mat-chip-list[@aria-orientation='horizontal']/div/mat-chip")
    account_btn = (By.XPATH, "//mat-nav-list[@role='navigation']/a[2]")
    #account_search = (By.XPATH, "//input[@data-placeholder='Search account']")
    #fleetdashboard = (By.XPATH, "//button[@mattooltip='Launch fleet dashboard']")
    fleetdashboard = (By.XPATH, "//button[@mattooltip='Launch fleet dashboard']")
    toggle_menu = (By.XPATH, "//mat-icon[normalize-space()='menu']")
    side_menu = (By.XPATH, "//div[contains(@class, 'mat-drawer-inner-container')]")

    def close_popup(self):
        time.sleep(5)
        try:
            self.driver.find_element(*MasterPortalPage.feature_announce_btn).is_displayed()
            feature_announcement = self.driver.find_element(*MasterPortalPage.feature_announce_btn).text
            self.driver.find_element(*MasterPortalPage.closebtn).click()
            print(feature_announcement)
        except:
            print("Popup not displayed in master page")
            time.sleep(3)
            tsp_name = self.driver.find_element(*MasterPortalPage.toolbar_menu).text
            print("TSP_name is " + tsp_name)
            time.sleep(1)
            version_num = self.driver.find_element(*MasterPortalPage.version_number).text
            print(version_num)
            time.sleep(1)

    def account_option(self):
        # time.sleep(5)
        # Ensure sidebar is expanded (Fix by Vidya Hampiholi - handles collapsed menu on Windows/Jenkins)
        self.ensure_sidebar_expanded(MasterPortalPage.side_menu, MasterPortalPage.toggle_menu)
        wait = WebDriverWait(self.driver, 20)
        account_btn = wait.until(EC.element_to_be_clickable(MasterPortalPage.account_btn))
        account_btn.click()
        print(self.driver.current_url)
        #time.sleep(3)
        #self.driver.find_element(*MasterPortalPage.account_search).click()
        #time.sleep(3)
        #self.driver.find_element(*MasterPortalPage.account_search).send_keys('Coogee-Chemicals')
        time.sleep(7)
        self.driver.find_element(*MasterPortalPage.fleetdashboard).click()
        time.sleep(12)
        second_window_Name = self.driver.current_window_handle
        second_window_Name1 = self.driver.window_handles[1]
        third_Window = self.driver.window_handles[2]
        self.driver.switch_to.window(third_Window)
        self.driver.switch_to.window(self.driver.window_handles[2])
        print(self.driver.current_url)
        print(self.driver.title)
        time.sleep(5)
        return self.driver.title

    def close_popup1(self):
        time.sleep(5)
        try:
            self.driver.find_element(*MasterPortalPage.feature_announce_btn).is_displayed()
            feature_announcement = self.driver.find_element(*MasterPortalPage.feature_announce_btn).text
            self.driver.find_element(*MasterPortalPage.closebtn).click()
            print(feature_announcement)
        except:
            print("Popup not displayed in fleet page")
            time.sleep(3)
            fleet_name = self.driver.find_element(*MasterPortalPage.toolbar_menu_fleet).text
            print("FleetName is " + fleet_name)
            time.sleep(1)
            version_num = self.driver.find_element(*MasterPortalPage.version_number).text
            print(version_num)
            time.sleep(1)

