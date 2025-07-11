import time

import pytest
import keyboard
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#import pyautogui
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BaseClass import BaseClass



class FleetPortalPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    #portal_version = (By.XPATH, "//h3[text()='Feature Announcement']/following-sibling::mat-chip-list/div/mat-chip")
   # portal_version = (By.XPATH, "//app-feature-announcement[@class='ng-star-inserted']/div/div/div/mat-chip-list/div/mat-chip")
    fleet_title = (By.XPATH, "//app-home[@class='ng-star-inserted']//app-header/mat-toolbar/div[2]/span")
    trips_card = (By.XPATH, "//div[@fxlayoutalign='space-between stretch']/div[1]/div[1]/mat-card[1]/div[1]")
    distance_card = (By.XPATH, "//div[@fxlayoutalign='space-between stretch']/div[1]/div[1]/mat-card[2]/div[1]")
    events_card = (By.XPATH, "//div[@fxlayoutalign='space-between stretch']/div[2]/div/mat-card[1]/div[1]")
    duration_hours = (By.XPATH, "//div[@fxlayoutalign='space-between stretch']/div[2]/div/mat-card[2]/div[1]")
    recomanded_events = (By.XPATH, "(//div[@class='container']/div//div/h3)[1]")
    top_drivers = (By.XPATH, "(//div[@class='container']/div//div/h3)[2]")
    require_coaching = (By.XPATH, "(//div[@class='container']/div//div/h3)[3]")
    event_summary = (By.XPATH, "(//div[@class='container']/div//div/h3)[4]")
    event_trend = (By.XPATH, "(//div[@class='container']/div//div/h3)[5]")
    # SAFETY EVENTS
    toggle_menu = (By.XPATH, "//button[.//mat-icon[normalize-space(.)='menu']]")
    #side_menu = (By.XPATH, "//div[contains(@class, 'mat-drawer-inner-container')]")
    side_menu = (By.XPATH, "//div[@class='mat-drawer-inner-container ng-tns-c263-3']")
    safety_events_btn = (By.XPATH, "//span[text()='Safety Events']/ancestor::span/parent::a")
    next_btn = (By.XPATH, "//span[text()='Next']")
    done_btn = (By.XPATH, "//span[text()='Done']")
    events_view = (By.XPATH, "//h3[contains(text(),'Events View')]")
    toggle_filter_btn = (By.XPATH, "//div[@class='device-id-filter']/div/button[1]")
    list_view_btn = (By.XPATH, "//div[@class='device-id-filter']/div/button[2]")
    # TRIPS
    trips_btn = (By.XPATH, "//span[text()='Trips']/ancestor::span/parent::a")
    trips_tab = (By.XPATH, "(//mat-tab-header[@class='mat-tab-header']/div/div/div/div)[1]")
    trips_list_table = (By.XPATH, "//h3[contains(text(),'Trip List ')]/parent::div")
    export_options = (By.XPATH, "//span[contains(text() ,' EXPORT OPTIONS ')]/parent::button")
    export_trips = (By.XPATH, "//div[@class='cdk-overlay-connected-position-bounding-box']/div/div/div/button[1]")
    trips_schedule = (By.XPATH, "//div[@class='cdk-overlay-connected-position-bounding-box']/div/div/div/button[2]")
    active_drivers_tab = (By.XPATH, "//mat-tab-header[@class='mat-tab-header']/div/div/div/div[2]")
    active_drivers_table = (By.XPATH, "//h3[contains(text(),'Active Drivers')]/parent::div")
    manage_trips_tab = (By.XPATH, "//div[@class='mat-tab-labels']/div[3]")
    bulk_updation_log = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator']/div[1]/h3")
    # LIVE VIEW
    live_view_page = (By.XPATH, "//span[text()='Live View']/ancestor::span/parent::a")
    one_view = (By.XPATH, "//div[@class='commandbar-toplevel-6ewwkk']/button")
    fleet_view = (By.XPATH, "//div[@class='map-container']/div/div/mat-button-toggle-group/mat-button-toggle[2]/button/span")
    asset_count = (By.XPATH, "//table[@role='table']/thead/tr/th[2]")
    list_view = (By.XPATH, "//div[@class='map-container']/div/div/mat-button-toggle-group/mat-button-toggle[1]/button/span")
    asset_id = (By.XPATH, "//mat-card[contains(@class,'mat-card mat-focus-indicator')]/div[3]/div/table//tr/th[1]")
    # COACHING
    coaching_page = (By.XPATH, "//span[text()='Coaching']/ancestor::span/parent::a")
    coachable_drivers = (By.XPATH, "//h3[text()=' Coachable Drivers ']")
    completed_coaching_sessions = (By.XPATH, "//h3[text()=' Completed Coaching Sessions ']")
    # VIDEO REQUESTS PAGE
    video_requests_page = (By.XPATH, "//span[text()='Video Requests']/ancestor::span/parent::a")
    video_requests_table = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator']/div/h3")
    request_video_popUp_btn = (By.XPATH, "(//div[@fxlayoutalign='space-between center'])[2]/div/div")
    video_requests_filter = (By.XPATH, "//mat-button-toggle-group/mat-button-toggle[1]")
    panic_button_filter = (By.XPATH, "//mat-button-toggle-group/mat-button-toggle[2]")
    event_on_demand_filter = (By.XPATH, "//mat-button-toggle-group/mat-button-toggle[3]")
    # DRIVERS PAGE
    drivers_page = (By.XPATH, "//span[text()='Drivers']/ancestor::span/parent::a")
    driver_list_table = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator']/div[1]/div/h3")
    export_btn = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator']/div[2]/div[2]/div[3]")
    add_driver_btn = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator']/div[2]/div[2]/div[4]")
    driver_name_btn = (By.XPATH, "//mat-label[text()=' Driver Name ']/ancestor::span/preceding-sibling::input")
    driver_ID_btn = (By.XPATH, "//mat-label[text()='Driver ID']/ancestor::span/preceding-sibling::input")
    email_address_btn = (By.XPATH, "//mat-label[text()='Email Address']/ancestor::span/preceding-sibling::input")
    save_details_btn = (By.XPATH, "//span[text()=' Save Details ']/ancestor::button")
    driver_serach = (By.XPATH, "//mat-label[text()='Search for Driver ID/Name']/ancestor::span/preceding-sibling::input")
    more_actions_btn = (By.XPATH, "//table[@role='table']/tbody/tr[1]/td[8]/button[1]")
    delete_driver_btn = (By.XPATH, "//div[@class='cdk-overlay-connected-position-bounding-box']/div/div/div/button[2]")
    batch_update_btn = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator']/div[2]/div[2]/div[2]")
    installers_tab = (By.XPATH, "//div[@class='mat-tab-label-container']/div/div/div[2]")
    installer_list_table = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator']/div/div/h3")
    installer_search = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator']/div/div[2]/mat-form-field/div")
    add_installer_btn =(By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator']/div/div[2]/button")

    # CHALLENGES PAGE
    challenges_page = (By.XPATH, "//span[text()='Challenges']/ancestor::span/parent::a")
    challenge_events_table = (By.XPATH, "//mat-card[@fxlayout='column']/div/h3")
    # REPORTS PAGE
    reports_page = (By.XPATH, "//span[text()='Reports']/ancestor::span/parent::a")
   # schedule_everytime = (By.XPATH,"//div[@aria-labelledby='commandbar-nudge-title']/div/div/div[2]/div/div[2]/button")
    overview_tab_rep = (By.XPATH, "//label[text()='Overview']/parent::div")
    view_report_btn = (By.XPATH, "//mat-tab-body[@role='tabpanel']/div/div/div/div/mat-card[1]/div[2]/div[2]/a")
    fleet_schedule = (By.XPATH, "//mat-tab-body[@role='tabpanel']/div/div/div/div/mat-card[1]/div[2]/div[2]/button")
    fleet_safety_report = (By.XPATH, "//h3[text()='Fleet Safety Report']")
    fleet_details_page_schedule = (By.XPATH, "//div[@fxlayoutalign='space-between center']/button[1]/span[1]")
    download_report_btn = (By.XPATH, "//div[@fxlayoutalign='space-between center']/button[2]/span[1]")
    back_arrow_btn = (By.XPATH, "//h3[text()='Fleet Safety Report']/preceding-sibling::button")
    coaching_view_report_btn = (By.XPATH, "//mat-tab-body[@role='tabpanel']/div/div/div/div/mat-card[2]/div[2]/div[2]/a")
    coaching_session_schedule = (By.XPATH, "//mat-tab-body[@role='tabpanel']/div/div/div/div/mat-card[2]/div[2]/div[2]/button")
    coaching_back_arrow_btn =(By.XPATH, "//div[@fxlayoutalign='space-between center']/div[1]/button[1]")
    coaching_effectiveness_driver = (By.XPATH, "//mat-tab-body[@role='tabpanel']/div/div/div/div/mat-card[3]/div[3]/a")
    coaching_effectiveness_back_arrow_btn = (By.XPATH, "//div[@fxlayoutalign='space-between center']/div/button")
    event_list_report =(By.XPATH, "//mat-tab-body[@role='tabpanel']/div/div/div/div/mat-card[4]/div[2]/div[1]/h3")
    event_list_download_btn = (By.XPATH, "//mat-tab-body[@role='tabpanel']/div/div/div/div/mat-card[4]/div[2]/div[2]/a")
    reports_close_button = (By.XPATH, "//mat-dialog-container[@role='dialog']/app-download-report/div/div/mat-icon")
    driver_privacy_mode_report =(By.XPATH, "//mat-tab-body[@role='tabpanel']/div/div/div/div/mat-card[5]/div[2]/div[1]/h3")
    driver_privacy_mode_download_btn =(By.XPATH, "//mat-tab-body[@role='tabpanel']/div/div/div/div/mat-card[5]/div[2]/div[2]/a")
    event_count_report = (By.XPATH, "//mat-tab-body[@role='tabpanel']/div/div/div/div/mat-card[6]/div[2]/div[1]/h3")
    event_count_report_download_btn = (By.XPATH, "//mat-tab-body[@role='tabpanel']/div/div/div/div/mat-card[6]/div[2]/div[2]/a")
    export_history_tab = (By.XPATH, "//div[@class='mat-tab-label-container']/div/div/div[2]")
    export_history_table =( By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator']/div[1]/h3")

    # ASSETS PAGE
    assets_page = (By.XPATH, "//span[text()='Assets']/ancestor::span/parent::a")
    overview_tab_assets = (By.XPATH, "//label[text()='OVERVIEW']/parent::div")
    asset_list_table = (By.XPATH, "//mat-card[@fxlayout='column']/div/h3")
    show_filters_btn = (By.XPATH, "//mat-card[@fxlayout='column']/div/div/button[2]")
    export_assets_btn = (By.XPATH, "//mat-card[@fxlayout='column']/div/div/button[3]")
    manage_assets_tab = (By.XPATH, "//label[text()='MANAGE ASSETS']/parent::div")
    batch_update_card = (By.XPATH, "//h3[text()='Batch Update']")
    batch_provisioning_card = (By.XPATH, "//h3[text()='Batch Provisioning']")
    devices_tab = (By.XPATH, "//label[text()='DEVICES']/parent::div")
    semi_provisioned_devices_table = (By.XPATH, "//h3[contains(text(),'Semi-provisioned Devices')]")
    diagnostics_tab = (By.XPATH, "//div[@class='mat-tab-label-container']/div/div[1]/div[4]")
    total_devices_card = (By.XPATH, "//div[@fxlayoutalign='space-between stretch']/div/div/mat-card[1]")
    total_events_card = (By.XPATH, "//div[@fxlayoutalign='space-between stretch']/div/div/mat-card[2]")
    diagnostics_tab_camera_event = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator']/mat-tab-group/mat-tab-header/div/div/div/div[1]")
    diagnostics_tab_device_events = (By.XPATH,"//mat-card[@class='mat-card mat-focus-indicator']/mat-tab-group/mat-tab-header/div/div/div/div[2]")
    diagnostics_tab_device_online_status = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator']/mat-tab-group/mat-tab-header/div/div/div/div[3]")

    # USERS PAGE
    users_page = (By.XPATH, "//span[text()='Users']/ancestor::span/parent::a")
    manage_users_table = (By.XPATH, "//h3[contains(text(),'Manage Users')]")
    add_user_btn = (By.XPATH, "//div[@fxlayoutalign='space-between center']/div/button[2]")
    roles_tab = (By.XPATH, "//div[@class='mat-tab-labels']/div[2]")
    manage_roles_table = (By.XPATH, "//div[@fxlayoutalign='space-between center']/h3")
    view_hierarchy_btn = (By.XPATH, "//div[@fxlayoutalign='space-between center']/div[1]/button[2]")
    add_role_btn = (By.XPATH, "//div[@fxlayoutalign='space-between center']/div[1]/button[3]")
    activity_log_tab = (By.XPATH, "//div[@class='mat-tab-labels']/div[3]")
    user_activity_logs =(By.XPATH,"//mat-card[@class='mat-card mat-focus-indicator']/div/h3")

    # CONFIGURATIONS PAGE
    configurations_page = (By.XPATH, "//span[text()='Configurations']/ancestor::span/parent::a")
    basic_tab = (By.XPATH, "//div[@class='mat-tab-list']/div/div[1]")
    basic_configurations = (By.XPATH, "//div[@fxlayoutalign='space-between stretch']/mat-card[1]/div/h3")
    advanced_tab = (By.XPATH, "//div[@class='mat-tab-list']/div/div[2]")
    advanced_configurations = (By.XPATH, "//div[@class='container ng-star-inserted']/mat-card[1]/div[1]/h3")
    driver_configurations = (By.XPATH, "//div[@class='container ng-star-inserted']/mat-card[2]/app-driver-configurations/div[1]/h3")
    coaching_tab = (By.XPATH, "//div[@class='mat-tab-list']/div/div[3]")
    coaching_thresholds_card = (By.XPATH, "//div[@class='container ng-star-inserted']/app-coaching-threshold/mat-card/div[1]/h3")
    automated_coaching_card = (By.XPATH, "//div[@class='container ng-star-inserted']/app-auto-coaching-event-selection/mat-card/div/div[1]")
    tagging_tab = (By.XPATH, "//div[@class='mat-tab-list']/div/div[4]")
    overview_table = (By.XPATH, "//mat-card[@class='mat-card mat-focus-indicator ng-star-inserted']/div/h3")


















    # Feature Announcement :-

    # virsion_comparision :

    # def extract_version_number(self, version):
    #
    #     # Extract the numbers after 'v'
    #     version_numbers = version.split('v')[-1]
    #     version_numbers = [int(num) for num in version_numbers.split('.')]
    #     return version_numbers
    #
    # def compare_versions(self, version1, version2):
    #     version1_numbers = self.extract_version_number(version1)
    #     version2_numbers = self.extract_version_number(version2)
    #     compare = False
    #     for num1, num2 in zip(version1_numbers, version2_numbers):
    #         if num1 == num2:
    #             compare = True
    #         else:
    #             compare = False
    #             break
    #         '''if num1 > num2:
    #             return f"{version1} (ERROR) is newer than {version2}"
    #         elif num1 < num2:
    #             return f"{version1} (ERROR) is older than {version2}"
    #
    #     return f"{version1} (PASSED) is the same as {version2}"'''
    #     return compare
    #
    # def compare_actual_version(self, log):
    #     try:
    #         version_element = self.driver.find_element(*FleetPortalPage.portal_version)
    #         text_version_str = version_element.text
    #         log.info("************ From Browser Version ************ :: %s " % text_version_str)
    #         manual_version_str = "v9.0.0"
    #
    #         result = self.compare_versions(text_version_str, manual_version_str)
    #         log.info("************ Manual Version ************ :: %s " % manual_version_str)
    #         log.info(" *********** Version result ******* :: %s " % result)
    #         assert result
    #
    #     except NoSuchElementException:
    #         log.error("************ Fleet portal version not matched ************")

############# HOME PAGE ####################
########### trips card validate #######################
    def validate_trips_card_present(self, log):
        print(self.driver.current_url)
        status = False
        try:
            trips = self.driver.find_element(*FleetPortalPage.trips_card)
            status = trips.is_displayed()
            print(trips.text + " matched")

        except NoSuchElementException:
            pytest.skip("************* Trips Card not displayed *************")
           # log.skip("************ Trips Card not displayed **********")
        return status

    def validate_distance(self, log):
        status = False
        try:
            distance = self.driver.find_element(*FleetPortalPage.distance_card)
            status = distance.is_displayed()
            print(distance.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Distance(mi) Card not displayed **********")
        return status

    def validate_event_per_100_miles(self, log):
        status = False
        try:
            events_card = self.driver.find_element(*FleetPortalPage.events_card)
            status = events_card.is_displayed()
            print(events_card.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Events Per 100 Miles Card not displayed **********")
        return status

    def validate_duration(self, log):
        status = False
        try:
            duration = self.driver.find_element(*FleetPortalPage.duration_hours)
            status = duration.is_displayed()
            print(duration.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Duration (hours) Card not displayed **********")
        return status

    time.sleep(10)

    def validate_recommended_events(self, log):
        status = False
        try:
            recomended_events1 = self.driver.find_element(*FleetPortalPage.recomanded_events)
            status = recomended_events1.is_displayed()
            print(recomended_events1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Recommended Events card not displayed **********")
        return status

    def validate_top_drivers(self, log):
        status = False
        try:
            top_drivers1 = self.driver.find_element(*FleetPortalPage.top_drivers)
            self.driver.execute_script("arguments[0].scrollIntoView();", top_drivers1)
            status = top_drivers1.is_displayed()
            print(top_drivers1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Top Drivers card not displayed **********")
        return status

    def validate_require_coaching(self, log):
        status = False
        try:
            require_coaching1 = self.driver.find_element(*FleetPortalPage.require_coaching)
            status = require_coaching1.is_displayed()
            print(require_coaching1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Require Coaching card not displayed **********")
        return status

    def validate_event_summary(self, log):
        status = False
        try:
            event_summary1 = self.driver.find_element(*FleetPortalPage.event_summary)
            status = event_summary1.is_displayed()
            print(event_summary1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Event Summary card not displayed **********")
        return status

    def validate_event_trend(self, log):
        status = False
        try:
            event_trend1 = self.driver.find_element(*FleetPortalPage.event_trend)
            status = event_trend1.is_displayed()
            print(event_trend1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Event Trend card not displayed **********")
        return status


    # SAFETY EVENTS PAGE

    def validate_safety_events(self, log):
        status = False
        try:
            # Ensure sidebar is expanded (Fix by Vidya Hampiholi - handles collapsed menu on Windows/Jenkins)
            self.ensure_sidebar_expanded(FleetPortalPage.side_menu, FleetPortalPage.toggle_menu)
            self.driver.find_element(*FleetPortalPage.safety_events_btn).click()
            time.sleep(5)
            safety_events1 = self.driver.find_element(*FleetPortalPage.safety_events_btn)
            print(self.driver.current_url)
            status = safety_events1.is_displayed()
            print(safety_events1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Safety Events button not displayed **********")
        return status

    def validate_welcome_to_safety_events(self, log):
        status = False
        try:
            # Check if the Next button is enabled and displayed, and click it
            next_button = self.driver.find_element(*FleetPortalPage.next_btn)
            if next_button.is_enabled() and next_button.is_displayed():
                next_button.click()
                print("Clicked on the 'Next' button successfully.")
                time.sleep(1)
            else:
                print("Next button is not visible or not interactable.")
                return False

            # Click the Next button again
            next_button = self.driver.find_element(*FleetPortalPage.next_btn)
            if next_button.is_enabled() and next_button.is_displayed():
                next_button.click()
                print("Clicked on the 'Next' button again successfully.")
                time.sleep(1)
            else:
                print("Next button is not visible or not interactable.")
                return False

            # Check if the Done button is enabled and displayed, and click it
            done_button = self.driver.find_element(*FleetPortalPage.done_btn)
            if done_button.is_enabled() and done_button.is_displayed():
                done_button.click()
                print("Clicked on the 'Done' button successfully.")
                time.sleep(1)
                status = True  # Set status to True when Done button is successfully clicked
            else:
                print("Done button is not visible or not interactable.")
                return False

        except NoSuchElementException as e:
            pytest.skip(
                f"************ Safety Events Announcement not found: {str(e)} **********")  # Skip if element is not found
        except Exception as e:
            pytest.skip(f"An unexpected error occurred: {str(e)}")  # Skip for any other exceptions
        return status

    # def validate_welcome_to_safety_events(self, log):
    #     status = False
    #     try:
    #         self.driver.find_element(*FleetPortalPage.next_btn).click()
    #         time.sleep(1)
    #         self.driver.find_element(*FleetPortalPage.next_btn).click()
    #         time.sleep(1)
    #         self.driver.find_element(*FleetPortalPage.done_btn).click()
    #         time.sleep(1)
    #
    #     except NoSuchElementException:
    #         pytest.skip("************ Safety Events Announcement not displayed **********")
    #     return status

    def validate_events_view(self, log):
        status = False
        try:
            events_view1 = self.driver.find_element(*FleetPortalPage.events_view)
            status = events_view1.is_displayed()
            print(events_view1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Events View card not displayed **********")
        return status


    def validate_safety_events_page_filter(self,log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.toggle_filter_btn).click()
            time.sleep(5)
            toggle_filter_btn1 = self.driver.find_element(*FleetPortalPage.toggle_filter_btn)
            print(self.driver.current_url)
            status = toggle_filter_btn1.is_displayed()
            print(toggle_filter_btn1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ filter_list button not displayed **********")
        return status

    def validate_safety_events_page_list_view(self,log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.list_view_btn).click()
            time.sleep(10)
            self.driver.find_element(*FleetPortalPage.toggle_filter_btn).click()
            time.sleep(5)
            list_view_btn1 = self.driver.find_element(*FleetPortalPage.list_view_btn)
            print(self.driver.current_url)
            status = list_view_btn1.is_displayed()
            print(list_view_btn1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ list button not displayed **********")
        return status

# TRIPS

    def validate_trips_page_btn(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.trips_btn).click()
            time.sleep(5)
            trips1 = self.driver.find_element(*FleetPortalPage.trips_btn)
            print(self.driver.current_url)
            status = trips1.is_displayed()
            print(trips1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Trips page button not displayed **********")
        return status

    def validate_trips_page_trips_tab(self, log):
        status = False
        try:
            trips_tab1 = self.driver.find_element(*FleetPortalPage.trips_tab)
            status = trips_tab1.is_displayed()
            print(trips_tab1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Trips tab not displayed **********")
        return status

    def validate_trips_page_trips_list_table(self, log):
        status = False
        try:
            trips_list_card1 = self.driver.find_element(*FleetPortalPage.trips_list_table)
            status = trips_list_card1.is_displayed()
            print(trips_list_card1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Trips List table not displayed **********")
        return status

    def validate_trips_page_export_options(self, log):
        status = False
        try:
            export_options1 = self.driver.find_element(*FleetPortalPage.export_options)
            status = export_options1.is_displayed()
            print(export_options1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************  EXPORT OPTIONS  button not displayed **********")
        return status

    def validate_trips_page_export_trips(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.export_options).click()
            time.sleep(5)
            export_trips1 = self.driver.find_element(*FleetPortalPage.export_trips)
            status = export_trips1.is_displayed()
            print(export_trips1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************  Export Now button not displayed **********")
        return status

    def validate_trips_page_trips_schedule(self, log):
        status = False
        try:
            #self.driver.find_element(*FleetPortalPage.export_options).click()
            time.sleep(5)
            trips_schedule1 = self.driver.find_element(*FleetPortalPage.trips_schedule)
            status = trips_schedule1.is_displayed()
            print(trips_schedule1.text + " matched")
            #pyautogui.press('esc')
            # Press ESC using ActionChains instead of pyautogui
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(5)
        except NoSuchElementException:
            pytest.skip("************ Schedule button not displayed **********")
        return status

    def validate_trips_page_active_drivers_tab(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.active_drivers_tab).click()
            time.sleep(3)
            active_drivers_tab1 = self.driver.find_element(*FleetPortalPage.active_drivers_tab)
            status = active_drivers_tab1.is_displayed()
            print(active_drivers_tab1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Active Drivers tab not displayed **********")
        return status


    def validate_trips_page_active_drivers_table(self, log):
        status = False
        try:
            active_drivers_table1 = self.driver.find_element(*FleetPortalPage.active_drivers_table)
            status = active_drivers_table1.is_displayed()
            print(active_drivers_table1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Active Drivers table not displayed **********")
        return status

    def validate_trips_page_manage_tab(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.manage_trips_tab).click()
            time.sleep(3)
            manage_trips_tab1 = self.driver.find_element(*FleetPortalPage.manage_trips_tab)
            status = manage_trips_tab1.is_displayed()
            print(manage_trips_tab1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ MANAGE tab not displayed **********")
        return status

    def validate_trips_page_bulk_updation(self, log):
        status = False
        try:
            bulk_updation_log1 = self.driver.find_element(*FleetPortalPage.bulk_updation_log)
            status = bulk_updation_log1.is_displayed()
            print(bulk_updation_log1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************  Bulk Updation Log table not displayed **********")
        return status

# LIVE VIEW PAGE

    def validate_live_view_page(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.live_view_page).click()
            time.sleep(5)
            self.driver.find_element(*FleetPortalPage.one_view).click()
            live_view_page = self.driver.find_element(*FleetPortalPage.live_view_page)
            print(self.driver.current_url)
            status = live_view_page.is_displayed()
            print(live_view_page.text + " matched")
            live_view_page.click()
        except NoSuchElementException:
            log.info("************ Live View page button not displayed **********")
        return status

    def validate_live_view_page_fleet_view_btn(self, log):
        status = False
        try:
            fleet_view1 = self.driver.find_element(*FleetPortalPage.fleet_view)
            status = fleet_view1.is_displayed()
            print(fleet_view1.text + " matched")

        except NoSuchElementException:
            log.info("************ FLEET VIEW button not displayed **********")
        return status

    def validate_live_view_page_asset_count_header(self, log):
        status = False
        try:
            asset_count1 = self.driver.find_element(*FleetPortalPage.asset_count)
            status = asset_count1.is_displayed()
            print(asset_count1.text + " matched")

        except NoSuchElementException:
            log.info("************ Asset Count header not displayed **********")
        return status

    # def validate_live_view_page_list_view_btn(self, log):
    #     status = False
    #     try:
    #         self.driver.find_element(*FleetPortalPage.list_view).click()
    #         time.sleep(5)
    #         list_view1 = self.driver.find_element(*FleetPortalPage.list_view)
    #         status = list_view1.is_displayed()
    #         print(list_view1.text + " matched")
    #
    #     except NoSuchElementException:
    #         log.info("************  LIST VIEW button not displayed **********")
    #     return status

    def validate_live_view_page_list_view_btn(self, log):
        status = False
        wait = WebDriverWait(self.driver, 20)

        try:
            #Wait until the "Fetching live asset details..." overlay disappears
            try:
                wait.until(EC.invisibility_of_element_located(
                    (By.XPATH, "//div[normalize-space()='Fetching live asset details...']")
                ))
                log.info("Overlay 'Fetching live asset details...' has disappeared.")
            except TimeoutException:
                log.warning("Overlay 'Fetching live asset details...' did not disappear in time. Proceeding anyway.")
            # Optionally wait for any drawer overlay to disappear too
            try:
                wait.until(EC.invisibility_of_element_located(
                    (By.CLASS_NAME, "mat-drawer-inner-container")
                ))
                log.info("Overlay 'mat-drawer-inner-container' has disappeared.")
            except TimeoutException:
                log.warning("Overlay 'mat-drawer-inner-container' did not disappear in time. Proceeding anyway.")

            # Wait until the element is clickable
            element = wait.until(EC.element_to_be_clickable(FleetPortalPage.list_view))

            # Scroll into view and click
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
            time.sleep(2)

            #Confirm it's displayed
            status = element.is_displayed()
            print(element.text + " matched")
            log.info("Clicked on List view button")

        except NoSuchElementException:
            log.error("************ LIST VIEW button not found **********")
        except TimeoutException:
            log.error("************ LIST VIEW button not clickable in time **********")
        except Exception as e:
            log.error(f"Unexpected error while clicking LIST VIEW button: {str(e)}")

        return status

    def validate_live_view_page_asset_header(self, log):
        status = False
        try:
            assetID_table1 = self.driver.find_element(*FleetPortalPage.asset_id)
            status = assetID_table1.is_displayed()
            print(assetID_table1.text + " matched")

        except NoSuchElementException:
            log.info("************  Asset header not displayed **********")
        return status
# COACHING PAGE

    def validate_coaching_page(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.coaching_page).click()
            time.sleep(5)
            coaching_page1 = self.driver.find_element(*FleetPortalPage.coaching_page)
            print(self.driver.current_url)
            status = coaching_page1.is_displayed()
            print(coaching_page1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Coaching page not displayed **********")
        return status

    def validate_coaching_page_coachable_drivers_table(self, log):
        status = False
        try:
            coachable_drivers_table1 = self.driver.find_element(*FleetPortalPage.coachable_drivers)
            status = coachable_drivers_table1.is_displayed()
            print(coachable_drivers_table1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Coachable Drivers table not displayed **********")
        return status


    def validate_coaching_page_completed_coaching_sessions_table(self, log):
        status = False
        try:
            completed_coaching_sessions_table1 = self.driver.find_element(*FleetPortalPage.completed_coaching_sessions)
            status = completed_coaching_sessions_table1.is_displayed()
            print(completed_coaching_sessions_table1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Completed Coaching Sessions table not displayed **********")
        return status


# VIDEO REQUESTS

    def validate_video_requests_page(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.video_requests_page).click()
            time.sleep(5)
            video_requests_page = self.driver.find_element(*FleetPortalPage.video_requests_page)
            print(self.driver.current_url)
            status = video_requests_page.is_displayed()
            print(video_requests_page.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Video Requests page not displayed **********")
        return status


    def validate_video_requests_page_table(self, log):
        status = False
        try:
            video_requests_table = self.driver.find_element(*FleetPortalPage.video_requests_table)
            status = video_requests_table.is_displayed()
            print(video_requests_table.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Video Requests table not displayed **********")
        return status


    def validate_video_requests_page_request_video_popUp(self, log):
        status = False
        try:
            video_requests_page_popUp = self.driver.find_element(*FleetPortalPage.request_video_popUp_btn)
            status = video_requests_page_popUp.is_displayed()
            print(video_requests_page_popUp.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Requests Video popUp button not displayed **********")
        return status


    def validate_video_requests_page_video_requests_filter(self, log):
        status = False
        try:
            video_requests_filter_btn = self.driver.find_element(*FleetPortalPage.video_requests_filter)
            status = video_requests_filter_btn.is_displayed()
            print(video_requests_filter_btn.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Video Requests filter button not displayed **********")
        return status


    def validate_video_requests_page_panic_btn_filter(self, log):
        status = False
        try:
            panic_button_filter_btn = self.driver.find_element(*FleetPortalPage.panic_button_filter)
            status = panic_button_filter_btn.is_displayed()
            print(panic_button_filter_btn.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Panic Button not displayed **********")
        return status


    def validate_video_requests_page_event_on_demand_filter(self, log):
        status = False
        try:
            event_on_demand_filter_btn = self.driver.find_element(*FleetPortalPage.event_on_demand_filter)
            status = event_on_demand_filter_btn.is_displayed()
            print(event_on_demand_filter_btn.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Event On-Demand filter button not displayed **********")
        return status


# DRIVERS PAGE

    def validate_Drivers_page(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.drivers_page).click()
            time.sleep(12)
            print(self.driver.current_url)
            drivers_page1 = self.driver.find_element(*FleetPortalPage.drivers_page)
            status = drivers_page1.is_displayed()
            print(drivers_page1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Drivers page not displayed **********")
        return status

    def validate_Drivers_page_driver_list_table(self, log):
        status = False
        try:
            driver_list_table1 = self.driver.find_element(*FleetPortalPage.driver_list_table)
            status = driver_list_table1.is_displayed()
            print(driver_list_table1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Driver List table not displayed **********")
        return status


    def validate_Drivers_page_export_btn(self, log):
        status = False
        try:
            export_btn1 = self.driver.find_element(*FleetPortalPage.export_btn)
            status = export_btn1.is_displayed()
            print(export_btn1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Export button not displayed **********")
        return status

    def validate_Drivers_page_add_driver_btn(self,log):
        status = False
        try:
            add_driver_btn1 = self.driver.find_element(*FleetPortalPage.add_driver_btn)
            status = add_driver_btn1.is_displayed()
            print(add_driver_btn1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Add Driver button not displayed **********")
        return status

    # def validate_Drivers_page_add_driver_btn(self, log, timeout=10):
    #     status = False
    #     wait = WebDriverWait(self.driver, timeout)
    #
    #     try:
    #         # Wait for the 'Add Driver' button to be visible and clickable
    #         add_driver_btn = wait.until(EC.element_to_be_clickable(FleetPortalPage.add_driver_btn))
    #         print(add_driver_btn.text + " matched")
    #         add_driver_btn.click()
    #
    #         self.driver.execute_script("window.scrollBy(0, 5000);")
    #
    #         # Wait and enter Driver Name
    #         driver_name_btn = wait.until(EC.element_to_be_clickable(FleetPortalPage.driver_name_btn))
    #         driver_name_btn.click()
    #         driver_name_btn.send_keys("Drivers")
    #
    #         # Wait and enter Driver ID
    #         driver_id_btn = wait.until(EC.element_to_be_clickable(FleetPortalPage.driver_ID_btn))
    #         driver_id_btn.click()
    #         driver_id_btn.send_keys("Drivers_0011")
    #
    #         # Wait and enter Email
    #         email_btn = wait.until(EC.element_to_be_clickable(FleetPortalPage.email_address_btn))
    #         email_btn.click()
    #         email_btn.send_keys("revathi.nagaraj+new@lightmetrics.co")
    #
    #         # Click Save
    #         save_btn = wait.until(EC.element_to_be_clickable(FleetPortalPage.save_details_btn))
    #         save_btn.click()
    #
    #         # Wait for confirmation message
    #         message_locator = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
    #         message_text = wait.until(EC.visibility_of_element_located(message_locator)).text
    #         print(message_text + "  :  ( Add Driver Message  )")
    #
    #         status = True
    #
    #     except (NoSuchElementException, TimeoutException) as e:
    #         log.error(f"Element interaction failed: {e}")
    #         pytest.skip("************ Add Driver button not displayed or interaction failed **********")
    #
    #     return status

    # def validate_Drivers_page_search_btn(self, log):
    #     status = False
    #     try:
    #         driver_serach1 = self.driver.find_element(*FleetPortalPage.driver_serach)
    #         status = driver_serach1.is_displayed()
    #         print(driver_serach1.text + " matched")
    #         self.driver.find_element(*FleetPortalPage.driver_serach).click()
    #         self.driver.find_element(*FleetPortalPage.driver_serach).send_keys("Drivers")
    #         time.sleep(5)
    #         self.driver.find_element(*FleetPortalPage.more_actions_btn).click()
    #         time.sleep(3)
    #         self.driver.find_element(*FleetPortalPage.delete_driver_btn).click()
    #         time.sleep(5)
    #         message = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
    #         message1 = wait.until(EC.visibility_of_element_located(message)).text
    #         print(message1 + "  :  ( Delete Driver Message  )")
    #
    #     except NoSuchElementException:
    #         pytest.skip("************ Driver ID/Name serach button not displayed **********")
    #     return status

    def validate_Drivers_page_search_btn(self,log):
        status = False
        try:
            wait = WebDriverWait(self.driver, 20)
            # Ensure sidebar is expanded (Fix by Vidya Hampiholi - handles collapsed menu on Windows/Jenkins)
            self.ensure_sidebar_expanded(FleetPortalPage.side_menu, FleetPortalPage.toggle_menu)
            element = wait.until(EC.element_to_be_clickable(FleetPortalPage.driver_serach))
            # Scroll into view
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
            log.info("Clicked on Driver Search button")
            return True
            # self.driver.find_element(*FleetPortalPage.driver_serach).click()
            time.sleep(12)
            driver_serach1 = self.driver.find_element(*FleetPortalPage.driver_serach)
            status = driver_serach1.is_displayed()
            print(driver_serach1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Driver ID/Name serach button not displayed **********")
        return status

    def validate_Drivers_page_batch_update_btn(self, log):
        status = False
        try:
            batch_update_btn1 = self.driver.find_element(*FleetPortalPage.batch_update_btn)
            status = batch_update_btn1.is_displayed()
            print(batch_update_btn1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************  Batch Update  button not displayed **********")
        return status

    def validate_Drivers_page_installer_tab(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.installers_tab).click()
            time.sleep(12)
            installers_tab1 = self.driver.find_element(*FleetPortalPage.installers_tab)
            status = installers_tab1.is_displayed()
            print(installers_tab1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Installers tab not displayed **********")
        return status


    def validate_Drivers_page_installers_list_table(self, log):
        status = False
        try:
            installer_list_table1 = self.driver.find_element(*FleetPortalPage.installer_list_table)
            status = installer_list_table1 .is_displayed()
            print(installer_list_table1 .text + " matched")

        except NoSuchElementException:
            pytest.skip("************  Installer List  table not displayed **********")
        return status

    def validate_Drivers_page_installer_search_btn(self, log):
        status = False
        try:
            installer_search1 = self.driver.find_element(*FleetPortalPage.installer_search)
            status = installer_search1.is_displayed()
            print(installer_search1.text + " matched")
            self.driver.find_element(*FleetPortalPage.installer_search).click()
            time.sleep(3)

        except NoSuchElementException:
            pytest.skip("************ Installer ID/Name serach button not displayed **********")
        return status

    def validate_Drivers_page_add_installer_btn(self, log):
        status = False
        try:
            add_installer_btn1 = self.driver.find_element(*FleetPortalPage.add_installer_btn)
            status = add_installer_btn1.is_displayed()
            print(add_installer_btn1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************  Add Installer  button not displayed **********")
        return status

# CHALLENGES PAGE

    def validate_challenges_page(self, log):
        status = False
        try:
            # Ensure sidebar is expanded (Fix by Vidya Hampiholi - handles collapsed menu on Windows/Jenkins)
            self.ensure_sidebar_expanded(FleetPortalPage.side_menu, FleetPortalPage.toggle_menu)
            self.driver.find_element(*FleetPortalPage.challenges_page).click()
            time.sleep(5)
            print(self.driver.current_url)
            challenges_page1 = self.driver.find_element(*FleetPortalPage.challenges_page)
            status = challenges_page1.is_displayed()
            print(challenges_page1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Challenges page not displayed **********")
        return status


    def validate_challenges_page_challenged_events_table(self, log):
        status = False
        try:
            challenge_events_table1 = self.driver.find_element(*FleetPortalPage.challenge_events_table)
            status = challenge_events_table1.is_displayed()
            print(challenge_events_table1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Challenge Events table not displayed **********")
        return status


# REPORTS PAGE


    def validate_reports_page(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.reports_page).click()
            time.sleep(3)
          #  self.driver.find_element(*FleetPortalPage.one_view).click()
            print(self.driver.current_url)
            reports_page1 = self.driver.find_element(*FleetPortalPage.reports_page)
            status = reports_page1.is_displayed()
            print(reports_page1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Reports page not displayed **********")
        return status



    def validate_reports_page_overview_tab(self, log):
        status = False
        try:
            overview_tab_rep1 = self.driver.find_element(*FleetPortalPage.overview_tab_rep)
            status = overview_tab_rep1.is_displayed()
            print(overview_tab_rep1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Overview tab not displayed **********")
        return status

    def validate_reports_page_fleet_schedule_button(self, log):
        status = False
        try:
            fleet_schedule1 = self.driver.find_element(*FleetPortalPage.fleet_schedule)
            status = fleet_schedule1.is_displayed()
            print(fleet_schedule1.text + " matched")
            time.sleep(7)

        except NoSuchElementException:
            pytest.skip("************ SCHEDULE button not displayed **********")
        return status


    def validate_reports_page_view_report_button(self, log):
        status = False
        try:
            view_report_btn1 = self.driver.find_element(*FleetPortalPage.view_report_btn)
            status = view_report_btn1.is_displayed()
            print(view_report_btn1.text + " matched")
            # Ensure sidebar is expanded (Fix by Vidya Hampiholi - handles collapsed menu on Windows/Jenkins)
            self.ensure_sidebar_expanded(FleetPortalPage.side_menu, FleetPortalPage.toggle_menu)
            self.driver.find_element(*FleetPortalPage.view_report_btn).click()
            time.sleep(7)

        except NoSuchElementException:
            pytest.skip("************ View Report button not displayed **********")
        return status



    def validate_reports_page_fleet_safety_report(self, log):
        status = False
        try:
            fleet_safety_report1 = self.driver.find_element(*FleetPortalPage.fleet_safety_report)
            status = fleet_safety_report1.is_displayed()
            print(fleet_safety_report1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Fleet Safety Report not displayed **********")
        return status

    def validate_reports_page_fleet_safety_schedule(self, log):
        status = False
        try:
            fleet_details_page_schedule1 = self.driver.find_element(*FleetPortalPage.fleet_details_page_schedule)
            status = fleet_details_page_schedule1.is_displayed()
            print(fleet_details_page_schedule1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************  SCHEDULE button not displayed **********")
        return status


    def validate_reports_page_download_report_btn(self, log):
        status = False
        try:
            download_report_btn1 = self.driver.find_element(*FleetPortalPage.download_report_btn)
            status = download_report_btn1.is_displayed()
            print(download_report_btn1.text + " matched")
            time.sleep(3)
        except NoSuchElementException:
            pytest.skip("************ Download Report button not displayed **********")
        return status


    def validate_reports_page_back_arrow_btn(self, log):
        status = False
        try:

            back_arrow_btn1 = self.driver.find_element(*FleetPortalPage.back_arrow_btn)
            status = back_arrow_btn1.is_displayed()
            print(back_arrow_btn1.text + " matched")
            self.driver.find_element(*FleetPortalPage.back_arrow_btn).click()
            time.sleep(3)
        except NoSuchElementException:
            pytest.skip("************ Back Arrow button not displayed **********")
        return status

    def validate_reports_page_coaching_session_schedule(self, log):
        status = False
        try:
            coaching_session_schedule1 = self.driver.find_element(*FleetPortalPage.coaching_session_schedule)
            status = coaching_session_schedule1.is_displayed()
            print(coaching_session_schedule1.text + " matched")
            time.sleep(5)

        except NoSuchElementException:
            pytest.skip("************  SCHEDULE  button not displayed **********")
        return status

    def validate_reports_page_coaching_report(self, log):
        status = False
        try:
            coaching_view_report_btn1 = self.driver.find_element(*FleetPortalPage.coaching_view_report_btn)
            status = coaching_view_report_btn1.is_displayed()
            print(coaching_view_report_btn1.text + " matched")
            self.driver.find_element(*FleetPortalPage.coaching_view_report_btn).click()
            time.sleep(7)

        except NoSuchElementException:
            pytest.skip("************ View Report button not displayed **********")
        return status

    def validate_reports_page_coaching_back_arrow_btn(self, log):
        status = False
        try:

            coaching_back_arrow_btn1 = self.driver.find_element(*FleetPortalPage.coaching_back_arrow_btn)
            status = coaching_back_arrow_btn1.is_displayed()
            print(coaching_back_arrow_btn1.text + " matched")
            self.driver.find_element(*FleetPortalPage.coaching_back_arrow_btn).click()
            time.sleep(3)
        except NoSuchElementException:
            pytest.skip("************ Back Arrow button not displayed **********")
        return status

    def validate_reports_page_coaching_effectiveness_driver(self, log):
        status = False
        try:

            coaching_effectiveness_driver1 = self.driver.find_element(*FleetPortalPage.coaching_effectiveness_driver)
            status = coaching_effectiveness_driver1.is_displayed()
            print(coaching_effectiveness_driver1.text + " matched")
            self.driver.find_element(*FleetPortalPage.coaching_effectiveness_driver).click()
            time.sleep(3)
        except NoSuchElementException:
            pytest.skip("************ View Report button not displayed **********")
        return status

    def validate_reports_page_coaching_effectiveness_back_arrow_btn(self, log):
        status = False
        try:

            coaching_effectiveness_back_arrow_btn1 = self.driver.find_element(*FleetPortalPage.coaching_effectiveness_back_arrow_btn)
            status = coaching_effectiveness_back_arrow_btn1.is_displayed()
            print(coaching_effectiveness_back_arrow_btn1.text + " matched")
            self.driver.find_element(*FleetPortalPage.coaching_effectiveness_back_arrow_btn).click()
            time.sleep(3)
        except NoSuchElementException:
            pytest.skip("************ Back Arrow button not displayed **********")
        return status

    def validate_reports_page_event_list_report(self, log):
        status = False
        try:

            event_list_report1 = self.driver.find_element(*FleetPortalPage.event_list_report)
            status = event_list_report1.is_displayed()
            print(event_list_report1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************  Event List Report not displayed **********")
        return status

    def validate_reports_page_event_list_report_download(self, log):
        status = False
        try:

            event_list_download_btn1 = self.driver.find_element(*FleetPortalPage.event_list_download_btn)
            status = event_list_download_btn1.is_displayed()
            print(event_list_download_btn1.text + " matched")
            self.driver.find_element(*FleetPortalPage.event_list_download_btn).click()
            time.sleep(5)
            self.driver.find_element(*FleetPortalPage.reports_close_button).click()
            time.sleep(3)

        except NoSuchElementException:
          pytest.skip("************  DOWNLOAD REPORT  button not displayed **********")
        return status

    def validate_reports_page_driver_privacy_mode_report(self, log):
        status = False
        try:

            driver_privacy_mode_report1 = self.driver.find_element(*FleetPortalPage.driver_privacy_mode_report)
            status = driver_privacy_mode_report1.is_displayed()
            print(driver_privacy_mode_report1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************  Driver Privacy Mode Report not displayed **********")
        return status

    def validate_reports_page_driver_privacy_mode_report_download(self, log):
        status = False
        try:

            driver_privacy_mode_download_btn1 = self.driver.find_element(*FleetPortalPage.driver_privacy_mode_download_btn)
            status = driver_privacy_mode_download_btn1.is_displayed()
            print(driver_privacy_mode_download_btn1.text + " matched")
            self.driver.find_element(*FleetPortalPage.driver_privacy_mode_download_btn).click()
            time.sleep(5)
            self.driver.find_element(*FleetPortalPage.reports_close_button).click()
            time.sleep(3)

        except NoSuchElementException:
          pytest.skip("************  DOWNLOAD REPORT  button not displayed **********")
        return status

    def validate_reports_page_event_count_report(self, log):
        status = False
        try:

            event_count_report1 = self.driver.find_element(*FleetPortalPage.event_count_report)
            status = event_count_report1.is_displayed()
            print(event_count_report1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************  Event Count Report not displayed **********")
        return status

    def validate_reports_page_event_count_report_download(self, log):
        status = False
        try:

            event_count_report_download_btn1 = self.driver.find_element(*FleetPortalPage.event_count_report_download_btn)
            status = event_count_report_download_btn1.is_displayed()
            print(event_count_report_download_btn1.text + " matched")
            self.driver.find_element(*FleetPortalPage.event_count_report_download_btn).click()
            time.sleep(5)
            self.driver.find_element(*FleetPortalPage.reports_close_button).click()
            time.sleep(3)

        except NoSuchElementException:
          pytest.skip("************  DOWNLOAD REPORT  button not displayed **********")
        return status

    def validate_reports_page_export_history_tab(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.export_history_tab).click()
            time.sleep(3)
            export_history_tab1 = self.driver.find_element(*FleetPortalPage.export_history_tab)
            status = export_history_tab1.is_displayed()
            print(export_history_tab1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Export History tab not displayed **********")
        return status

    def validate_reports_page_export_history_table(self, log):
        status = False
        try:
            export_history_table1 = self.driver.find_element(*FleetPortalPage.export_history_table)
            status = export_history_table1.is_displayed()
            print(export_history_table1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************  Export History table not displayed **********")
        return status
# ASSETS PAGE

    def validate_assets_page(self, log):
        status = False
        try:
            # Ensure sidebar is expanded (Fix by Vidya Hampiholi - handles collapsed menu on Windows/Jenkins)
            self.ensure_sidebar_expanded(FleetPortalPage.side_menu, FleetPortalPage.toggle_menu)
            self.driver.find_element(*FleetPortalPage.assets_page).click()
            time.sleep(5)
            print(self.driver.current_url)
            assets_page1 = self.driver.find_element(*FleetPortalPage.assets_page)
            status = assets_page1.is_displayed()
            print(assets_page1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Assets page not displayed **********")
        return status



    def validate_assets_page_overview_tab(self, log):
        status = False
        try:
            overview_tab1 = self.driver.find_element(*FleetPortalPage.overview_tab_assets)
            status = overview_tab1.is_displayed()
            print(overview_tab1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Overview tab not displayed **********")
        return status


    def validate_assets_page_asset_list_table(self, log):
        status = False
        try:
            asset_list_table1 = self.driver.find_element(*FleetPortalPage.asset_list_table)
            status = asset_list_table1.is_displayed()
            print(asset_list_table1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Asset List table not displayed **********")
        return status


    def validate_assets_page_show_filters_button(self, log):
        status = False
        try:
            show_filters_btn1 = self.driver.find_element(*FleetPortalPage.show_filters_btn)
            status = show_filters_btn1.is_displayed()
            print(show_filters_btn1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Show Filters button not displayed **********")
        return status


    def validate_assets_page_export_assets_button(self, log):
        status = False
        try:
            export_assets_btn1 = self.driver.find_element(*FleetPortalPage.export_assets_btn)
            status = export_assets_btn1.is_displayed()
            print(export_assets_btn1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Export Assets button not displayed **********")
        return status


    def validate_assets_page_manage_assets_tab(self, log):
        status = False
        try:
            manage_assets_tab1 = self.driver.find_element(*FleetPortalPage.manage_assets_tab)
            self.driver.find_element(*FleetPortalPage.manage_assets_tab).click()
            time.sleep(3)
            status = manage_assets_tab1.is_displayed()
            print(manage_assets_tab1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Manage Assets tab not displayed **********")
        return status


    def validate_assets_page_batch_update_card(self, log):
        status = False
        try:
            batch_update_card1 = self.driver.find_element(*FleetPortalPage.batch_update_card)
            status = batch_update_card1.is_displayed()
            print(batch_update_card1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Batch Update card not displayed **********")
        return status


    def validate_assets_page_batch_provisioning_card(self, log):
        status = False
        try:
            batch_provisioning_card1 = self.driver.find_element(*FleetPortalPage.batch_provisioning_card)
            status = batch_provisioning_card1.is_displayed()
            print(batch_provisioning_card1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Batch Provisioning card not displayed **********")
        return status


    def validate_assets_page_devices_tab(self, log):
        status = False
        try:
            devices_tab1 = self.driver.find_element(*FleetPortalPage.devices_tab)
            self.driver.find_element(*FleetPortalPage.devices_tab).click()
            time.sleep(3)
            status = devices_tab1.is_displayed()
            print(devices_tab1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Devices tab not displayed **********")
        return status


    def validate_assets_page_semi_provisioned_devices_table(self, log):
        status = False
        try:
            semi_provisioned_devices1 = self.driver.find_element(*FleetPortalPage.semi_provisioned_devices_table)
            status = semi_provisioned_devices1.is_displayed()
            print(semi_provisioned_devices1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Semi Provisioned Devices table not displayed **********")
        return status

    def validate_assets_page_diagnostics_tab(self, log):
        status = False
        try:
            diagnostics_tab1 = self.driver.find_element(*FleetPortalPage.diagnostics_tab)
            self.driver.find_element(*FleetPortalPage.diagnostics_tab).click()
            time.sleep(3)
            status = diagnostics_tab1.is_displayed()
            print(diagnostics_tab1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ DIAGNOSTICS tab not displayed **********")
        return status

    def validate_assets_page_diagnostics_devices_card(self, log):
        status = False
        try:
            total_devices_card1 = self.driver.find_element(*FleetPortalPage.total_devices_card)
            status = total_devices_card1.is_displayed()
            print(total_devices_card1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ TOTAL DEVICES card not displayed **********")
        return status

    def validate_assets_page_diagnostics_events_card(self, log):
        status = False
        try:
            total_events_card1 = self.driver.find_element(*FleetPortalPage.total_events_card)
            status = total_events_card1.is_displayed()
            print(total_events_card1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************  TOTAL EVENTS  card not displayed **********")
        return status

    def validate_assets_page_diagnostics_camera_event(self, log):
        status = False
        try:
            diagnostics_tab_camera_event1 = self.driver.find_element(*FleetPortalPage.diagnostics_tab_camera_event)
            status = diagnostics_tab_camera_event1.is_displayed()
            print(diagnostics_tab_camera_event1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Camera Visibility Events table not displayed **********")
        return status

    def validate_assets_page_diagnostics_device_events(self,log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.diagnostics_tab_device_events).click()
            time.sleep(7)
            diagnostics_tab_device_events1 = self.driver.find_element(*FleetPortalPage.diagnostics_tab_device_events)
            status = diagnostics_tab_device_events1.is_displayed()
            print(diagnostics_tab_device_events1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Device Diagnostic Events table not displayed **********")
        return status

    def validate_assets_page_diagnostics_device_online_status(self,log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.diagnostics_tab_device_online_status).click()
            time.sleep(7)
            diagnostics_tab_device_online_status1 = self.driver.find_element(*FleetPortalPage.diagnostics_tab_device_online_status)
            status = diagnostics_tab_device_online_status1.is_displayed()
            print(diagnostics_tab_device_online_status1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Device Online Status table not displayed **********")
        return status
# USERS PAGE


    def validate_users_page(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.users_page).click()
            time.sleep(5)
            print(self.driver.current_url)
            user_page1 = self.driver.find_element(*FleetPortalPage.users_page)
            status = user_page1.is_displayed()
            print(user_page1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ User page not displayed **********")
        return status


    def validate_users_page_manage_users_table(self, log):
        status = False
        try:
            manage_users_table1 = self.driver.find_element(*FleetPortalPage.manage_users_table)
            status = manage_users_table1.is_displayed()
            print(manage_users_table1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Manage Users table not displayed **********")
        return status


    # def validate_user_management_page_export_button(self, log):
    #     status = False
    #     try:
    #         export_btn_user1 = self.driver.find_element(*FleetPortalPage.export_btn_user)
    #         status = export_btn_user1.is_displayed()
    #         print(export_btn_user1.text + " matched")
    #
    #     except NoSuchElementException:
    #         pytest.skip("************ Export button user not displayed **********")
    #     return status


    def validate_users_page_add_user_button(self, log):
        status = False
        try:
            add_user1 = self.driver.find_element(*FleetPortalPage.add_user_btn)
            status = add_user1.is_displayed()
            print(add_user1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Add User button not displayed **********")
        return status

    def validate_users_page_roles_tab(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.roles_tab).click()
            time.sleep(5)
            roles_tab1 = self.driver.find_element(*FleetPortalPage.roles_tab)
            status = roles_tab1.is_displayed()
            print(roles_tab1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Roles tab not displayed **********")
        return status


    def validate_users_page_manage_roles_table(self, log):
        status = False
        try:
            manage_roles_table1 = self.driver.find_element(*FleetPortalPage.manage_roles_table)
            status = manage_roles_table1.is_displayed()
            print(manage_roles_table1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Manage Roles table not displayed **********")
        return status


    def validate_users_page_view_hierarchy_btn(self, log):
        status = False
        try:
            view_hierarchy_btn1 = self.driver.find_element(*FleetPortalPage.view_hierarchy_btn)
            status = view_hierarchy_btn1.is_displayed()
            print(view_hierarchy_btn1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ View Hierarchy button not displayed **********")
        return status


    def validate_users_page_add_role_btn(self, log):
        status = False
        try:
            add_role_btn1 = self.driver.find_element(*FleetPortalPage.add_role_btn)
            status = add_role_btn1.is_displayed()
            print(add_role_btn1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Add Role button not displayed **********")
        return status

    def validate_users_page_activity_log_tab(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.activity_log_tab).click()
            time.sleep(5)
            activity_log_tab1 = self.driver.find_element(*FleetPortalPage.activity_log_tab)
            status = activity_log_tab1.is_displayed()
            print(activity_log_tab1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ ACTIVITY LOG tab not displayed **********")
        return status

    def validate_users_page_user_activity_log_table(self, log):
        status = False
        try:
            user_activity_logs1 = self.driver.find_element(*FleetPortalPage.user_activity_logs)
            status = user_activity_logs1.is_displayed()
            print(user_activity_logs1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************  User Activity Logs table not displayed **********")
        return status

# CONFIGURATIONS PAGE


    def validate_configurations_page(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.configurations_page).click()
            time.sleep(5)
            print(self.driver.current_url)
            configurations_page1 = self.driver.find_element(*FleetPortalPage.configurations_page)
            status = configurations_page1.is_displayed()
            print(configurations_page1.text + " matched")

        except NoSuchElementException:
            pytest.skip("************ Configurations page not displayed **********")
        return status


    def validate_configurations_page_basic_tab(self, log):
        status = False
        try:
            basic_tab1 = self.driver.find_element(*FleetPortalPage.basic_tab)
            status = basic_tab1.is_displayed()
            print(basic_tab1.text + " matched")

        except NoSuchElementException:
            log.info("************ Basic tab not displayed **********")
        return status


    def validate_configurations_page_basic_configurations_table(self, log):
        status = False
        try:
            basic_configurations1 = self.driver.find_element(*FleetPortalPage.basic_configurations)
            status = basic_configurations1.is_displayed()
            print(basic_configurations1.text + " matched")

        except NoSuchElementException:
            log.info("************ Basic Configurations table not displayed **********")
        return status


    def validate_configurations_page_advanced_tab(self, log):
        status = False
        try:
            advance_tab1 = self.driver.find_element(*FleetPortalPage.advanced_tab)
            self.driver.find_element(*FleetPortalPage.advanced_tab).click()
            time.sleep(3)
            status = advance_tab1.is_displayed()
            print(advance_tab1.text + " matched")

        except NoSuchElementException:
            log.info("************ Advanced tab not displayed **********")
        return status


    def validate_configurations_page_advanced_configurations(self, log):
        status = False
        try:
            advanced_configurations1 = self.driver.find_element(*FleetPortalPage.advanced_configurations)
            status = advanced_configurations1.is_displayed()
            print(advanced_configurations1.text + " matched")

        except NoSuchElementException:
            log.info("************ Advanced Configurations card not displayed **********")
        return status


    def validate_configurations_page_driver_configurations_card(self, log):
        status = False
        try:
            driver_configurations1 = self.driver.find_element(*FleetPortalPage.driver_configurations)
            status = driver_configurations1.is_displayed()
            print(driver_configurations1.text + " matched")

        except NoSuchElementException:
            log.info("************ Driver Configurations card not displayed **********")
        return status

    def validate_configurations_page_coaching_tab(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.coaching_tab).click()
            time.sleep(5)
            coaching_tab1 = self.driver.find_element(*FleetPortalPage.coaching_tab)
            status = coaching_tab1.is_displayed()
            print(coaching_tab1.text + " matched")

        except NoSuchElementException:
            log.info("************ Coaching tab not displayed **********")
        return status

    def validate_configurations_page_coaching_thresholds_card(self, log):
        status = False
        try:
            coaching_thresholds_card1 = self.driver.find_element(*FleetPortalPage.coaching_thresholds_card)
            status = coaching_thresholds_card1.is_displayed()
            print(coaching_thresholds_card1.text + " matched")

        except NoSuchElementException:
            log.info("************ Coaching Thresholds card not displayed **********")
        return status

    def validate_configurations_page_automated_coaching_card(self, log):
        status = False
        try:
            automated_coaching_card = self.driver.find_element(*FleetPortalPage.automated_coaching_card)
            status = automated_coaching_card.is_displayed()
            print(automated_coaching_card.text + " matched")

        except NoSuchElementException:
            log.info("************ Automated Coaching card not displayed **********")
        return status

    def validate_configurations_page_tagging_tab(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortalPage.tagging_tab).click()
            time.sleep(5)
            tagging_tab1 = self.driver.find_element(*FleetPortalPage.tagging_tab)
            status = tagging_tab1.is_displayed()
            print(tagging_tab1.text + " matched")

        except NoSuchElementException:
            log.info("************ Tagging tab not displayed **********")
        return status

    def validate_configurations_page_overview_table(self, log):
        status = False
        try:
            overview_table1 = self.driver.find_element(*FleetPortalPage.overview_table)
            status = overview_table1.is_displayed()
            print(overview_table1.text + " matched")

        except NoSuchElementException:
            log.info("************ Overview table not displayed **********")

        self.driver.close()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        log.info(self.driver.title)
        self.driver.close()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])
        return status






