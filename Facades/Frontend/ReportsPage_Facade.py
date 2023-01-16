from Pages.Reports_Page import Reports_Page

class ReportsPage_Facade:

    def __init__(self, page, testData, environmentConfigs):
        self.page = page
        self.testData = testData
        self.environmentConfigs = environmentConfigs
        self.reports_page = Reports_Page(self.page, self.testData, self.environmentConfigs)

    def validate_report_name(self, generated_report_name):
        self.reports_page.reports_button.click()
        ui_report_name = self.reports_page.report_name_ui.text_content()
        assert generated_report_name == ui_report_name, f"Generated report name = {generated_report_name} != ui_report_name = {ui_report_name}"
        self.reports_page.report_name_ui.click()