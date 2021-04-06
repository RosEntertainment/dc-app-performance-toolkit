import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.confluence.pages.pages import Login, AllUpdates
from util.conf import CONFLUENCE_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_pages']:
        app_specific_page_id = datasets['custom_page_id']

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out
    # @print_timing("selenium_app_specific_user_login")
    # def measure():
    #     def app_specific_user_login(username='admin', password='admin'):
    #         login_page = Login(webdriver)
    #         login_page.delete_all_cookies()
    #         login_page.go_to()
    #         login_page.wait_for_page_loaded()
    #         login_page.set_credentials(username=username, password=password)
    #         login_page.click_login_button()
    #         if login_page.is_first_login():
    #             login_page.first_user_setup()
    #         all_updates_page = AllUpdates(webdriver)
    #         all_updates_page.wait_for_page_loaded()
    #     app_specific_user_login(username='admin', password='admin')
    # measure()

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("selenium_app_custom_action:view_page")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/pages/viewpage.action?pageId={app_specific_page_id}")
            page.wait_until_visible((By.ID, "title-text"))  # Wait for title field visible
            page.wait_until_visible((By.CLASS_NAME, "toDoListApp"))  # Wait for you app-specific UI element by ID selector
            page.wait_until_visible((By.CLASS_NAME, "toDoReportContainer"))
        sub_measure()

        @print_timing("selenium_app_custom_action:create_todo")
        def sub_measure():
            page.get_element((By.CLASS_NAME, "addTaskButton")).click()

            inputElement = page.get_element((By.XPATH, '//input[@placeholder="Insert a new task"]'))
            inputElement.send_keys('ToDo1')
            inputElement.send_keys(Keys.ENTER)
        sub_measure()

        @print_timing("selenium_app_custom_action:view_todo")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/pages/viewpage.action?pageId={app_specific_page_id}")
            page.wait_until_visible((By.CLASS_NAME, "tickTaskButton"))
        sub_measure()
        
        # @print_timing("selenium_app_custom_action:view_page")
        # def sub_measure():
            # page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/pages/viewpage.action?pageId={app_specific_page_id}")
            # page.wait_until_visible((By.ID, "title-text"))  # Wait for title field visible
            # page.wait_until_visible((By.XPATH, "//*[@data-macro-name='rate-me-macro']"))  # Wait for you app-specific UI element by ID selector
            # page.wait_until_visible((By.XPATH, "//*[@data-macro-name='rate-me-top-macro']"))
        # sub_measure()

        # @print_timing("selenium_app_custom_action:view_profile_page")
        # def sub_measure():
            # page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/plugins/rate/me/rateMeProfile.action")
            # page.wait_until_visible((By.CLASS_NAME, "title"))
        # sub_measure()
        
        # @print_timing("selenium_app_custom_action:view_clean_users_page")
        # def sub_measure():
            # page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/plugins/cleaner/usersGlobalConfiguration.action")
            # page.wait_until_visible((By.CLASS_NAME, "cleanerUsersDiv"))
        # sub_measure()

        # @print_timing("selenium_app_custom_action:view_clean_groups_page")
        # def sub_measure():
            # page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/plugins/cleaner/groupsGlobalConfiguration.action")
            # page.wait_until_visible((By.CLASS_NAME, "availableGroupsDiv"))
        # sub_measure()

        # @print_timing("selenium_app_custom_action:view_clean_spaces_page")
        # def sub_measure():
            # page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/plugins/cleaner/cleanerGlobalConfiguration.action")
            # page.wait_until_visible((By.CLASS_NAME, "space-input-label"))
        # sub_measure()
        
        # @print_timing("selenium_app_custom_action:view_clean_blogs_and_pages_page")
        # def sub_measure():
            # page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/plugins/cleaner/blogsPagesGlobalConfiguration.action")
            # page.wait_until_visible((By.CLASS_NAME, "space-input-label"))
        # sub_measure()

    measure()
