import time

import playwright
from playwright.sync_api import sync_playwright
from BaseClass.Frontend.BaseFrontendClass import BaseFacadeClass




class DashboardPage(BaseFacadeClass):

    def __init__(self, page, testData, environmentConfigs):
        self.page = page
        self.testData = testData
        self.environmentData = environmentConfigs
        # with sync_playwright() as p:
        #     with p.chromium.launch(headless=False) as browser:
        #         self.page = browser.new_page()
                # self.page.text_content()
        self.singleCompany_button = self.page.locator("//a[text()='Single Company']")
        self.search_company_name_input = self.page.locator('//input[@id="search-companies"]')
        self.searched_company_li_result_xpath = "//ul//button[1]//p[text()='ENGINEERED FOAM PRODUCTS LIMITED']"
        self.searched_company_li_button = self.page.locator(self.searched_company_li_result_xpath)
        self.generate_report_button = self.page.locator("//button[text()='Generate Report']")
        self.page_url = self.page.url
        self.summary = self.page.get_by_text('Summary')
        self.go_to_report_btn = self.page.locator("//button[text()='Go to report']")
        self.logout_button = self.page.locator("//a[text()='Logout']")

    def get_url(self):
        return self.page.evaluate('window.location.href')