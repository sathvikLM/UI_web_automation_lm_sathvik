import time

import pytest

from pageObjects.AdminPage import AdminPage
from pageObjects.FleetPortalPage import FleetPortalPage
from pageObjects.MasterPortalPage import MasterPortalPage
from utilities.BaseClass import BaseClass
from utilities.customLogger import LogGen


class Test_LM_Regression_Suite(BaseClass):
    logger = LogGen.loggen()

    @pytest.mark.parametrize("config", [ 'Lmpresales' ])
    def test_lm_regression_suite(self, config):
        log = self.getLogger()
        log.info("********************** admin login ***********************")

        adminPage = AdminPage(self.driver)
        title = adminPage.loginToAdminPage(log)
        time.sleep(10)
        mastertitle = adminPage.customer_tsp(log, config)
        log.info("********* master portal title *********** :: " + mastertitle)
        masterportalpage = MasterPortalPage(self.driver)
        masterportalpage.close_popup()
        fleetPortal_Title = masterportalpage.account_option()
        log.info("********** Fleet portal title ************ :: " + fleetPortal_Title)
        fleetportal = FleetPortalPage(self.driver)
        # fleetportal.compare_actual_version(log)
        time.sleep(3)
        masterportalpage.close_popup1()
        log.info("************ Fleet portal popup closed ************")
        tripstatus = fleetportal.validate_trips_card_present(log)
        log.info("************ Trips Card is present ************ :: %s " % tripstatus)
        distance_status = fleetportal.validate_distance(log)
        log.info("************ Distance (mi) presents ************ :: %s " % distance_status)
        event_status = fleetportal.validate_event_per_100_miles(log)
        log.info("************ Events Per 100 Miles presents ************ :: %s " % event_status)
        duration_status = fleetportal.validate_duration(log)
        log.info("************ Duration (hours) card presents ************ :: %s " % duration_status)
        recommended_status = fleetportal.validate_recommended_events(log)
        # log.info("{}{}".format("************ Recommended events present ************ ", recommended_status))
        log.info("************ Recommended Events card present ************ :: %s " % recommended_status)
        top_drivers_status = fleetportal.validate_top_drivers(log)
        log.info("************ Top Drivers card present ************ :: %s " % top_drivers_status)
        require_coaching_status = fleetportal.validate_require_coaching(log)
        log.info("********************** Require Coaching card presents *********************** :: %s " % require_coaching_status)
        event_summary_status = fleetportal.validate_event_summary(log)
        log.info("********************** Event Summary card presents *********************** :: %s " % event_summary_status)
        event_trend_status = fleetportal.validate_event_trend(log)
        log.info("********************** Event Trend card presents *********************** :: %s " % event_trend_status)
        safety_events_btn_status = fleetportal.validate_safety_events(log)
        log.info(
            "********************** Safety Events Button presents *********************** :: %s " % safety_events_btn_status)
        # Announcement_safety_events_btn_status = fleetportal.validate_welcome_to_safety_events(log)
        # log.info(
        #     "********************** Safety Events Commandbar presents *********************** :: %s " % Announcement_safety_events_btn_status)
        events_view_status = fleetportal.validate_events_view(log)
        log.info("********************** Events View card presents *********************** :: %s " % events_view_status)
        toggle_filter_btn_status = fleetportal.validate_safety_events_page_filter(log)
        log.info(
            "********************** filter_list Button presents *********************** :: %s " % toggle_filter_btn_status)
        list_view_btn_status = fleetportal.validate_safety_events_page_list_view(log)
        log.info(
            "********************** List Button presents *********************** :: %s " % list_view_btn_status)
        trips_status = fleetportal.validate_trips_page_btn(log)
        log.info("********************** Trips Button presents *********************** :: %s " % trips_status)
        trips_tab_status = fleetportal.validate_trips_page_trips_tab(log)
        log.info("********************** Trips Tab presents *********************** :: %s " % trips_tab_status)
        trips_list_table_status = fleetportal.validate_trips_page_trips_list_table(log)
        log.info(
            "********************** Trips List Table presents *********************** :: %s " % trips_list_table_status)
        export_options_status = fleetportal.validate_trips_page_export_options(log)
        log.info("**********************  EXPORT OPTIONS  presents *********************** :: %s " % export_options_status)
        export_trips_status = fleetportal.validate_trips_page_export_trips(log)
        log.info(
            "**********************  Export Now button  presents *********************** :: %s " % export_trips_status
        )
        trips_schedule_status = fleetportal.validate_trips_page_trips_schedule(log)
        log.info(
            "**********************  Schedule button  presents *********************** :: %s " % trips_schedule_status
        )
        active_drivers_tab_status = fleetportal.validate_trips_page_active_drivers_tab(log)
        log.info(
            "********************** Active Drivers Tab presents *********************** :: %s " % active_drivers_tab_status)
        active_drivers_table_status = fleetportal.validate_trips_page_active_drivers_table(log)
        log.info(
            "********************** Active Drivers Table presents *********************** :: %s " % active_drivers_table_status)
        trips_manage_tab_status = fleetportal.validate_trips_page_manage_tab(log)
        log.info(
            "********************** MANAGE Tab presents *********************** :: %s " % trips_manage_tab_status)
        bulk_updation_table_status = fleetportal.validate_trips_page_bulk_updation(log)
        log.info(
            "**********************  Bulk Updation Log table presents *********************** :: %s " % bulk_updation_table_status)
        live_view_page_status = fleetportal.validate_live_view_page(log)
        log.info("********************** Live View Page presents *********************** :: %s " % live_view_page_status)
        fleet_view_btn_status = fleetportal.validate_live_view_page_fleet_view_btn(log)
        log.info(
            "********************** FLEET VIEW button presents *********************** :: %s " % fleet_view_btn_status)
        asset_count_header_status = fleetportal.validate_live_view_page_asset_count_header(log)
        log.info(
            "********************** Asset Count header presents *********************** :: %s " % asset_count_header_status)
        live_view_page_list_view_btn_status = fleetportal.validate_live_view_page_list_view_btn(log)
        log.info(
            "********************** LIST VIEW button presents *********************** :: %s " % live_view_page_list_view_btn_status)
        asset_header_status = fleetportal.validate_live_view_page_asset_header(log)
        log.info("********************** Asset header presents *********************** :: %s " % asset_header_status)
        coaching_page_status = fleetportal.validate_coaching_page(log)
        log.info("********************** Coaching Page presents *********************** :: %s " % coaching_page_status)
        coachable_drivers_status = fleetportal.validate_coaching_page_coachable_drivers_table(log)
        log.info(
            "********************** Coachable Drivers Table presents *********************** :: %s " % coachable_drivers_status)
        completed_coaching_sessions_status = fleetportal.validate_coaching_page_completed_coaching_sessions_table(log)
        log.info(
            "********************** Completed Coaching Sessions Table presents *********************** :: %s " % completed_coaching_sessions_status)
        video_requests_page_status = fleetportal.validate_video_requests_page(log)
        log.info(
            "********************** Video Requests page presents *********************** :: %s " % video_requests_page_status)
        video_requests_table_status = fleetportal.validate_video_requests_page_table(log)
        log.info(
            "********************** Video Requests Table presents *********************** :: %s " % video_requests_table_status)
        request_video_popUp_status = fleetportal.validate_video_requests_page_request_video_popUp(log)
        log.info(
            "********************** Request Video popUp presents *********************** :: %s " % request_video_popUp_status)
        video_requests_filter_status = fleetportal.validate_video_requests_page_video_requests_filter(log)
        log.info(
            "********************** Video Requests filter presents *********************** :: %s " % video_requests_filter_status)
        panic_btn_filter_status = fleetportal.validate_video_requests_page_panic_btn_filter(log)
        log.info(
            "********************** Panic Button filter presents *********************** :: %s " % panic_btn_filter_status)
        event_on_demand_filter_status = fleetportal.validate_video_requests_page_event_on_demand_filter(log)
        log.info(
            "********************** Event On-Demand filter  presents *********************** :: %s " % event_on_demand_filter_status)
        drivers_page_status = fleetportal.validate_Drivers_page(log)
        log.info(
            "********************** Drivers page presents *********************** :: %s " % drivers_page_status)
        driver_list_table_status = fleetportal.validate_Drivers_page_driver_list_table(log)
        log.info(
            "********************** Driver List table presents *********************** :: %s " % driver_list_table_status)
        export_btn_status = fleetportal.validate_Drivers_page_export_btn(log)
        log.info("********************** Export button presents *********************** :: %s " % export_btn_status)
        add_driver_btn_status = fleetportal.validate_Drivers_page_add_driver_btn(log)
        log.info(
            "********************** Add Driver button presents *********************** :: %s " % add_driver_btn_status)
        driver_search_btn_status = fleetportal.validate_Drivers_page_search_btn(log)
        log.info(
            "********************** Driver ID/Name serach button presents *********************** :: %s " % driver_search_btn_status)
        driver_batch_update_btn_status = fleetportal.validate_Drivers_page_batch_update_btn(log)
        log.info(
            "**********************  Batch Update button presents *********************** :: %s " % driver_batch_update_btn_status)
        installer_tab_status = fleetportal.validate_Drivers_page_installer_tab(log)
        log.info(
            "********************** Installers tab presents *********************** :: %s " % installer_tab_status)
        installers_list_table_status = fleetportal.validate_Drivers_page_installers_list_table(log)
        log.info(
            "********************** Installer List  table presents *********************** :: %s " % installers_list_table_status
        )
        installer_search_btn_status = fleetportal.validate_Drivers_page_installer_search_btn(log)
        log.info(
            "********************** Installer ID/Name serach button presents *********************** :: %s " % installer_search_btn_status)
        add_installer_btn_status = fleetportal.validate_Drivers_page_add_installer_btn(log)
        log.info(
            "********************** Add Installer  button presents *********************** :: %s " % add_installer_btn_status)
        challenges_page_status = fleetportal.validate_challenges_page(log)
        log.info(
            "********************** Challenges page presents *********************** :: %s " % challenges_page_status)
        challenged_events_table_status = fleetportal.validate_challenges_page_challenged_events_table(log)
        log.info(
            "********************** Challenge Events table presents *********************** :: %s " % challenged_events_table_status)
        reports_page_status = fleetportal.validate_reports_page(log)
        log.info("********************** Reports page presents *********************** :: %s " % reports_page_status)
        overview_tab_status = fleetportal.validate_reports_page_overview_tab(log)
        log.info("********************** Overview tab presents *********************** :: %s " % overview_tab_status)
        fleet_schedule_btn_status = fleetportal.validate_reports_page_fleet_schedule_button(log)
        log.info(
            "********************** Fleet SCHEDULE  button presents *********************** :: %s " % fleet_schedule_btn_status
        )
        view_report_btn_status = fleetportal.validate_reports_page_view_report_button(log)
        log.info(
            "********************** Fleet Safety View Report button presents *********************** :: %s " % view_report_btn_status)
        fleet_safety_report_status = fleetportal.validate_reports_page_fleet_safety_report(log)
        log.info(
            "********************** Fleet Safety Report presents *********************** :: %s " % fleet_safety_report_status)
        fleet_safety_schedule_status = fleetportal.validate_reports_page_fleet_safety_schedule(log)
        log.info(
            "********************** Fleet Safety  SCHEDULE button presents *********************** :: %s " % fleet_safety_schedule_status
        )
        download_report_btn_status = fleetportal.validate_reports_page_download_report_btn(log)
        log.info(
            "********************** Download Report button presents *********************** :: %s " % download_report_btn_status)
        back_arrow_btn_status = fleetportal.validate_reports_page_back_arrow_btn(log)
        log.info(
            "********************** Back Arrow button presents *********************** :: %s " % back_arrow_btn_status)
        coaching_schedule_btn_status = fleetportal.validate_reports_page_coaching_session_schedule(log)
        log.info(
            "**********************  SCHEDULE  button presents *********************** :: %s " % coaching_schedule_btn_status
        )
        coaching_view_report_btn_status = fleetportal.validate_reports_page_coaching_report(log)
        log.info(
            "********************** Coaching Session View Report button presents *********************** :: %s " % coaching_view_report_btn_status)
        coaching_back_arrow_btn_status = fleetportal.validate_reports_page_coaching_back_arrow_btn(log)
        log.info(
            "********************** Back Arrow button presents *********************** :: %s " % coaching_back_arrow_btn_status)
        coaching_effectiveness_view_report_btn_status = fleetportal.validate_reports_page_coaching_effectiveness_driver(log)
        log.info(
            "********************** Coaching Effectiveness(Driver) View Report button presents *********************** :: %s " % coaching_effectiveness_view_report_btn_status)
        coaching_effectiveness_back_arrow_btn_status = fleetportal.validate_reports_page_coaching_effectiveness_back_arrow_btn(log)
        log.info(
            "********************** Back Arrow button presents *********************** :: %s " % coaching_effectiveness_back_arrow_btn_status)
        event_list_report_status = fleetportal.validate_reports_page_event_list_report(log)
        log.info(
            "********************** Event List Report card presents *********************** :: %s " % event_list_report_status)
        event_list_download_report_status = fleetportal.validate_reports_page_event_list_report_download(log)
        log.info(
            "********************** DOWNLOAD REPORT  button presents *********************** :: %s " % event_list_download_report_status)
        driver_privacy_mode_status = fleetportal.validate_reports_page_driver_privacy_mode_report(log)
        log.info(
            "********************** Driver Privacy Mode Report card presents *********************** :: %s " % driver_privacy_mode_status)
        driver_privacy_mode_download_report_status = fleetportal.validate_reports_page_driver_privacy_mode_report_download(log)
        log.info(
            "********************** DOWNLOAD REPORT  button presents *********************** :: %s " % driver_privacy_mode_download_report_status)
        event_count_report_status = fleetportal.validate_reports_page_event_count_report(log)
        log.info(
            "**********************  Event Count Report card presents *********************** :: %s " % event_count_report_status)
        event_count_download_report_status = fleetportal.validate_reports_page_event_count_report_download(log)
        log.info(
            "********************** DOWNLOAD REPORT  button presents *********************** :: %s " % event_count_download_report_status)
        export_history_tab_status = fleetportal.validate_reports_page_export_history_tab(log)
        log.info(
            "********************** Export History tab presents *********************** :: %s " % export_history_tab_status)
        export_history_table_status = fleetportal.validate_reports_page_export_history_table(log)
        log.info(
            "**********************  Export History table presents *********************** :: %s " % export_history_table_status)
        assets_page_status = fleetportal.validate_assets_page(log)
        log.info("********************** Assets page presents *********************** :: %s " % assets_page_status)
        overview_tab_status = fleetportal.validate_assets_page_overview_tab(log)
        log.info("********************** Overview tab presents *********************** :: %s " % overview_tab_status)
        asset_list_table_status = fleetportal.validate_assets_page_asset_list_table(log)
        log.info(
            "********************** Asset List table presents *********************** :: %s " % asset_list_table_status)
        show_filters_button_status = fleetportal.validate_assets_page_show_filters_button(log)
        log.info(
            "********************** Show Filters button presents *********************** :: %s " % show_filters_button_status)
        export_assets_button_status = fleetportal.validate_assets_page_export_assets_button(log)
        log.info(
            "********************** Export Assets button presents *********************** :: %s " % export_assets_button_status)
        manage_assets_tab_status = fleetportal.validate_assets_page_manage_assets_tab(log)
        log.info(
            "********************** Manage Assets tab presents *********************** :: %s " % manage_assets_tab_status)
        batch_update_card_status = fleetportal.validate_assets_page_batch_update_card(log)
        log.info(
            "********************** Batch Update card presents *********************** :: %s " % batch_update_card_status)
        batch_provisioning_card_status = fleetportal.validate_assets_page_batch_provisioning_card(log)
        log.info(
            "********************** Batch Provisioning card presents *********************** :: %s " % batch_provisioning_card_status)
        devices_tab_status = fleetportal.validate_assets_page_devices_tab(log)
        log.info("********************** Devices tab presents *********************** :: %s " % devices_tab_status)
        semi_provisioned_devices_table_status = fleetportal.validate_assets_page_semi_provisioned_devices_table(log)
        log.info(
            "********************** Semi Provisioned Devices table presents *********************** :: %s " % semi_provisioned_devices_table_status)
        diagnostics_tab_status = fleetportal.validate_assets_page_diagnostics_tab(log)
        log.info("********************** DIAGNOSTICS tab presents *********************** :: %s " % diagnostics_tab_status)
        diagnostics_tab_devices_card_status = fleetportal.validate_assets_page_diagnostics_devices_card(log)
        log.info(
            "********************** TOTAL DEVICES card presents *********************** :: %s " % diagnostics_tab_devices_card_status)
        diagnostics_tab_events_card_status = fleetportal.validate_assets_page_diagnostics_events_card(log)
        log.info(
            "**********************  TOTAL EVENTS  card presents *********************** :: %s " % diagnostics_tab_events_card_status)
        diagnostics_tab_camera_event_table_status = fleetportal.validate_assets_page_diagnostics_camera_event(log)
        log.info(
            "********************** Camera Visibility Events table presents *********************** :: %s " % diagnostics_tab_camera_event_table_status)
        diagnostics_tab_device_event_table_status = fleetportal.validate_assets_page_diagnostics_device_events(log)
        log.info(
            "********************** Device Diagnostic Events table presents *********************** :: %s " % diagnostics_tab_device_event_table_status)
        diagnostics_tab_device_online_status = fleetportal.validate_assets_page_diagnostics_device_online_status(log)
        log.info(
            "********************** Device Online Status table presents *********************** :: %s " % diagnostics_tab_device_online_status)
        user_page_status = fleetportal.validate_users_page(log)
        log.info(
            "********************** Users page presents *********************** :: %s " % user_page_status)
        manage_users_table_status = fleetportal.validate_users_page_manage_users_table(log)
        log.info(
            "********************** Manage Users table presents *********************** :: %s " % manage_users_table_status)
        add_user_button_status = fleetportal.validate_users_page_add_user_button(log)
        log.info(
            "********************** Add User button presents *********************** :: %s " % add_user_button_status)
        roles_tab_status = fleetportal.validate_users_page_roles_tab(log)
        log.info(
            "********************** Roles tab presents *********************** :: %s " % roles_tab_status)
        manage_roles_table_status = fleetportal.validate_users_page_manage_roles_table(log)
        log.info(
            "********************** Manage Roles table presents *********************** :: %s " % manage_roles_table_status)
        view_hierarchy_btn_status = fleetportal.validate_users_page_view_hierarchy_btn(log)
        log.info(
            "********************** View Hierarchy button presents *********************** :: %s " % view_hierarchy_btn_status)
        add_role_btn_status = fleetportal.validate_users_page_add_role_btn(log)
        log.info(
            "********************** Add Role button presents *********************** :: %s " % add_role_btn_status)
        activity_log_tab_status =fleetportal.validate_users_page_activity_log_tab(log)
        log.info(
            "********************** ACTIVITY LOG tab presents *********************** :: %s " % activity_log_tab_status)
        user_activity_table_status = fleetportal.validate_users_page_user_activity_log_table(log)
        log.info(
            "**********************  User Activity Logs table presents *********************** :: %s " % user_activity_table_status)
        configurations_page_status = fleetportal.validate_configurations_page(log)
        log.info(
            "********************** Configurations page presents *********************** :: %s " % configurations_page_status)
        basic_tab_status = fleetportal.validate_configurations_page_basic_tab(log)
        log.info(
            "********************** Basic tab presents *********************** :: %s " % basic_tab_status)
        basic_configurations_table_status = fleetportal.validate_configurations_page_basic_configurations_table(log)
        log.info(
            "********************** Basic Configurations table presents *********************** :: %s " % basic_configurations_table_status)
        advanced_tab_status = fleetportal.validate_configurations_page_advanced_tab(log)
        log.info(
            "********************** Advanced tab presents *********************** :: %s " % advanced_tab_status)
        advanced_configurations_card_status = fleetportal.validate_configurations_page_advanced_configurations(log)
        log.info(
            "********************** Advanced Configurations card presents *********************** :: %s " % advanced_configurations_card_status)
        driver_configurations_card_status = fleetportal.validate_configurations_page_driver_configurations_card(log)
        log.info(
            "********************** Driver Configurations card presents *********************** :: %s " % driver_configurations_card_status)
        coaching_tab_status = fleetportal.validate_configurations_page_coaching_tab(log)
        log.info(
            "********************** Coaching tab presents *********************** :: %s " % coaching_tab_status)
        coaching_thresholds_card_status = fleetportal.validate_configurations_page_coaching_thresholds_card(log)
        log.info(
            "********************** Coaching Thresholds card presents *********************** :: %s " % coaching_thresholds_card_status)
        automated_coaching_card_status = fleetportal.validate_configurations_page_automated_coaching_card(log)
        log.info(
            "********************** Automated Coaching card presents *********************** :: %s " % automated_coaching_card_status)
        tagging_tab_status = fleetportal.validate_configurations_page_tagging_tab(log)
        log.info(
            "********************** Tagging tab presents *********************** :: %s " % tagging_tab_status)
        overview_table_status = fleetportal.validate_configurations_page_overview_table(log)
        log.info(
            "********************** Overview table presents *********************** :: %s " % overview_table_status)
        adminPage.admin_Logout()
        log.info("************** Logout successful ****************")
        self.driver.quit()
        log.info("************** Browser closed successfully ****************")
