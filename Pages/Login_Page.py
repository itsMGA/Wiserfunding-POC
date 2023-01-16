import playwright
from playwright.sync_api import sync_playwright

from BaseClass.Frontend.BaseFrontendClass import BaseFacadeClass




class LoginPage(BaseFacadeClass):

    def __init__(self, testData, environmentConfigs, context):
        self.page = context
        self.testData = testData
        self.environmentData = environmentConfigs
        self.username_input = self.page.get_by_test_id("testid-email")
        self.password_input = self.page.get_by_test_id("testid-password")
        self.singIn_button = self.page.locator("//button[text()='Sign in']")
        self.welcome_back_header = self.page.locator("//p[text()='Welcome back,']")