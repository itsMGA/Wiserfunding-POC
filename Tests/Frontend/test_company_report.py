from playwright.sync_api import sync_playwright
from Facades.Frontend.LoginPage_Facade import LoginPage_Facade
from Facades.Frontend.DashboardPage_Facade import DashboardPage_Facade
from Facades.Frontend.ReportPage_Facade import ReportPage_Facade
from Facades.Frontend.ReportsPage_Facade import ReportsPage_Facade
from Facades.Frontend.SettingsPage_Facade import SettingsPage_Facade
from apps.utils import Ultilities
import pytest


@pytest.fixture(scope="session")
def page():
    pw = sync_playwright().start()
    br = pw.chromium.launch(headless=False)
    page = br.new_page()
    page.goto("https://alpha.wiserfunding.com/")
    yield page
    page.close()
    br.close()



class Test_Company_report():
    utils = Ultilities()

    @pytest.mark.wiserReport
    def test_company_report_vs_api_change_pass_relogin(self, testData, environmentConfigs, page):
        login_page = LoginPage_Facade(testData=testData, environmentConfigs=environmentConfigs, page=page)
        login_page.succesful_login()

        dashboard_page = DashboardPage_Facade(testData=testData, environmentConfigs=environmentConfigs, page=page)
        dashboard_page.generate_single_company_report().set_report_id()
        generated_report_name = dashboard_page.get_report_name()

        report_page = ReportPage_Facade(testData=testData, environmentConfigs=environmentConfigs, page=page)
        report_page.validate_page_report_header()\
            .validate_report_page_name()\
            .validate_summary_fields_vs_api(dashboard_page.get_report_id())

        reports_page = ReportsPage_Facade(testData=testData, environmentConfigs=environmentConfigs, page=page)
        reports_page.validate_report_name(generated_report_name)

        report_page.validate_page_report_header()\
            .validate_report_page_name()\

        settingsPage = SettingsPage_Facade(testData=testData, environmentConfigs=environmentConfigs, page=page)
        settingsPage.change_password()

        self.utils.shuffle_passwords()
        testData.data["password"], testData.data["new_pass"] = testData.data["new_pass"], testData.data["password"]

        dashboard_page.logout()

        login_page.succesful_login()

