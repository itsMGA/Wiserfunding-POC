import requests
import json



class Report_api_Facade():

    def __init__(self, testData, environmentConfigs):
        self.testData = testData
        self.environemnt = environmentConfigs

    def execute_successful_request(self, report_id):
        token_url = self.environemnt.auth2_token
        data = {
            "grant_type": "password",
            "username": self.testData.data["username"],
            "password": self.testData.data["password"],
        }
        token_rsp = requests.post(url=token_url, data=data)
        assert token_rsp.status_code == 200, f"Failed to request access token!\nStatus code {token_rsp.status_code} != 200"
        token = token_rsp.json()["access_token"]
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }

        report_api_url = self.environemnt.report_api
        report_api_url += f"/{report_id}"
        report_rsp = requests.get(url=report_api_url, headers=headers)

        assert report_rsp.status_code == 200, f"Failed to request access report!\nStatus code {report_rsp.status_code} != 200"
        return report_rsp.json()