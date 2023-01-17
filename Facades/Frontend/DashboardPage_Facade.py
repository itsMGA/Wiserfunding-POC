import time
from datetime import datetime
from datetime import timedelta
import pytz

from Pages.Dashboard_Page import DashboardPage

class DashboardPage_Facade:
    report_id = ''

    def __init__(self, page, testData, environmentConfigs):
        self.page = page
        self.testData = testData
        self.environmentConfigs = environmentConfigs
        self.dasboard_page = DashboardPage(self.page, self.testData, self.environmentConfigs)
    def generate_single_company_report(self):
        self.dasboard_page.singleCompany_button.click()
        self.dasboard_page.search_company_name_input.type(self.testData.data["company_name"])
        self.dasboard_page.page.click(self.dasboard_page.searched_company_li_result_xpath)
        self.dasboard_page.generate_report_button.click()
        self.dasboard_page.go_to_report_btn.click()
        #Wait until page loads, tied to header loading time
        self.dasboard_page.page.wait_for_selector("""//div[@data-playwright-id="reports.main.header"]//p[text()='Wiserfunding Risk Assessment Report']""")
        #redundant sleep, could be removed if page proves proper client side rendering
        time.sleep(2)
        return self

    def set_report_id(self):
        self.report_id = self.dasboard_page.get_url().split('/')[-1]
        return self

    def logout(self):
        self.dasboard_page.logout_button.click()
    def get_report_id(self):
        return self.report_id

    def get_report_date_fromat_for_tz(self):
        # Get the current time in the EEST timezone
        eest_tz = pytz.timezone("EET")
        current_time = datetime.now(eest_tz)

        formatted_time = current_time.strftime("%d-%m-%y-%H:%M")
        if current_time.tzname() == 'EET':
            # add 2 hours to the current time
            formatted_time = (datetime.strptime(formatted_time, '%d-%m-%y-%H:%M') + timedelta(hours=2)).strftime(
                '%d-%m-%y-%H:%M')
            return formatted_time
        else:
            return formatted_time

    def get_report_name(self):
        return f'{self.testData.data["company_name"]}-{self.get_report_date_fromat_for_tz()}'
