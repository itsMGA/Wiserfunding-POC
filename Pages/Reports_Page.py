import time

import playwright
from playwright.sync_api import sync_playwright
from BaseClass.Frontend.BaseFrontendClass import BaseFacadeClass




class Reports_Page(BaseFacadeClass):

    def __init__(self, page, testData, environmentConfigs):
        self.page = page
        self.testData = testData
        self.environmentData = environmentConfigs
        # with sync_playwright() as p:
        #     with p.chromium.launch(headless=False) as browser:
        #         self.page = browser.new_page()
        self.report_name_ui = self.page.locator("""//*[@data-testid="table-row-0"]/td[1]""")
        self.reports_button = self.page.locator("""//a[text()='Reports']""")
