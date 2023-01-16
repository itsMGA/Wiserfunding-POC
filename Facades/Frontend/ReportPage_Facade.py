from Pages.Report_Page import ReportPage
from Facades.APIs.report_api import Report_api_Facade

class ReportPage_Facade:

    def __init__(self, page, testData, environmentConfigs):
        self.page = page
        self.testData = testData
        self.environmentConfigs = environmentConfigs
        self.report_page = ReportPage(self.page, self.testData, self.environmentConfigs)
        self.report_api = Report_api_Facade(testData=self.testData, environmentConfigs=self.environmentConfigs)

    def validate_summary_fields_vs_api(self, report_id):
        report_api_Response = self.report_api.execute_successful_request(report_id)
        nace_sector_ui = self.report_page.nace_Sector.text_content()
        nace_code_ui = self.report_page.nace_code.text_content()
        company_desc_ui = self.report_page.company_desc.text_content()

        nace_sector_api = report_api_Response['details']['nace_name']
        nace_code_api = report_api_Response['details']['nace_code']
        company_desc_api = report_api_Response['details']['description']

        assert nace_sector_ui == nace_sector_api, f"{nace_sector_ui} != {nace_sector_api}"
        assert nace_code_ui == nace_code_api, f"{nace_code_ui} != {nace_code_api}"
        assert company_desc_ui == company_desc_api, f"{company_desc_ui} != {company_desc_api}"
        return self

    def validate_page_report_header(self):
        assert self.report_page.risk_assesment_report_label.text_content() == "Wiserfunding Risk Assessment Report", f"ui header {self.report_page.risk_assesment_report_label.text_content()} != Wiserfunding Risk Assessment Report"
        return self
    def validate_report_page_name(self):
        assert self.report_page.report_header_name.text_content() == self.testData.data['company_name'], f"ui report name {self.report_page.report_header_name.text_content()} != test data comp name{self.testData.data['company_name']}"
        return self