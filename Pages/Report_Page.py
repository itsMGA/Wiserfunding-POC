import time

import playwright
from playwright.sync_api import sync_playwright
from BaseClass.Frontend.BaseFrontendClass import BaseFacadeClass




class ReportPage(BaseFacadeClass):

    def __init__(self, page, testData, environmentConfigs):
        self.page = page
        self.testData = testData
        self.environmentData = environmentConfigs
        # with sync_playwright() as p:
        #     with p.chromium.launch(headless=False) as browser:
        #         self.page = browser.new_page()
        self.nace_Sector = self.page.locator("""//div[@data-playwright-id="reports.main.summary.details"]//h4[text()='NACE Sector']/parent::div/p""")
        self.company_desc = self.page.locator("""//div[@data-playwright-id="reports.main.summary.details"]//h4[text()='Company Description']/parent::div/p""")
        self.nace_code = self.page.locator("""//div[@data-playwright-id="reports.main.summary.details"]//h4[text()='NACE Code']/parent::div/p""")
        self.risk_assesment_report_label = self.page.locator("""//div[@data-playwright-id="reports.main.header"]//p[text()='Wiserfunding Risk Assessment Report']""")
        self.report_header_name = self.page.locator('//div[@data-playwright-id="reports.main.header"]//h1')
