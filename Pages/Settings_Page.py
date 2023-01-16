import time

import playwright
from playwright.sync_api import sync_playwright
from BaseClass.Frontend.BaseFrontendClass import BaseFacadeClass




class Settings_Page(BaseFacadeClass):

    def __init__(self, page, testData, environmentConfigs):
        self.page = page
        self.testData = testData
        self.environmentData = environmentConfigs
        # with sync_playwright() as p:
        #     with p.chromium.launch(headless=False) as browser:
        #         self.page = browser.new_page()
        #         self.page.get_by_test_id()
        self.report_name_ui = self.page.locator("""//*[@data-testid="table-row-0"]/td[1]""")
        self.reports_button = self.page.locator("""//a[text()='Reports']""")
        self.settings_button = self.page.locator("//a[text()='Settings']")
        self.save_btn = self.page.locator('//button[@data-playwright-id="settings.password.save_btn"]')
        self.current_pass_input = self.page.get_by_test_id("testid-currentPassword")
        self.new_pass = self.page.get_by_test_id("testid-newPassword")
        self.confirm_new_pass = self.page.get_by_test_id("testid-confirmPassword")

        self.succesfully_changed_password_notif = self.page.locator("//*[text()='Your password were updated successfully.']")