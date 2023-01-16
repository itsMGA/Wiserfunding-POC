import requests
from pytest_schema import schema, And, Optional, Or
from BaseClass.Frontend.BaseAPIClass import BaseFacadeClass


class Partner_Report_List_Facade(BaseFacadeClass):
    response = None
    device_Response = {}
    devices_Response = {}
    user_response = {}
    sessionByUser_response = {}
    sessionByCarrier_response = {}


    def __init__(self):
        pass

    def executeSuccessfulRequest(self, environmentConfigs, testData):
        url = environmentConfigs.partner_ReportList_URL

        headers = {
            "Authorization": f"Bearer {self.getAccessToken(environmentConfigs=environmentConfigs, testData=testData)}",
        }

        self.response = requests.get(url=url, headers=headers)
        # self.pretty_print_POST(self.response.request)
        # print(self.response.json())
        return self

    def executeNotAuthRequest(self, environmentConfigs, testData):
        url = environmentConfigs.partner_ReportList_URL


        headers = {
            "Authorization": f"Bearer ewqe213",
        }

        self.response = requests.get(url=url, headers=headers)
        # self.pretty_print_POST(self.response.request)
        # print(self.response.json())
        return self

    def validate_200_StatusCode(self):
        assert self.response.status_code == 200, f"Status code should be 200 'OK' but got status code = '{self.response.status_code}'"
        return self

    def validate_401_StatusCode(self):
        assert self.response.status_code == 401, f"Status code should be 401 'NOT_AUTHORIZED' but got status code = '{self.response.status_code}'"
        return self

    def validate_invalidParams_Schema(self):

        api_schema = {
            "result": "INVALID_PARAMS",
        }

        assert schema(api_schema) == self.response.json()
        return self

    def validateSuccessfulReq_Schema(self, testData):

        """{
result: enum
Allowed: OK┃NOT_FOUND
error: string
reports: [{
task_code: string
status: enum

NEW - task created
QUERYING - process of selecting the data
QUERYING_FAILED - process of selecting failed
EXPORTING - process of converting data to csv files
EXPORTING_FAILED - process of converting failed
COMPLETED - all process is done
FAILED - other error
REPORT_NOT_EXISTS - csv files not found
⤵
Allowed: NEW┃QUERYING┃QUERYING_FAILED┃EXPORTING┃EXPORTING_FAILED┃COMPLETED┃FAILED┃REPORT_NOT_EXISTS
description: string
report_urls: string
report_type: enum

BY_USER - find sessions by user id
BY_CARRIER - find sessions by date
BY_ALL_USERS - find users by carrier
BY_ALL_DEVICES - find devices bu carrier
BY_USER_ID - find user by id
BY_DEVICE_ID - find device by id
⤵
Allowed: BY_USER┃BY_CARRIER┃BY_ALL_USERS┃BY_ALL_DEVICES┃BY_USER_ID┃BY_DEVICE_ID
created_time: integer
carrier: string
start_time: integer
end_time: integer
}]
} """
        api_schema = {
                        "result": "OK",
                        "reports": [
                            {
                            "task_code": And(str, lambda s: len(s) > 1),
                            "status": Or("NEW", "QUERYING", "QUERYING_FAILED", "EXPORTING", "EXPORTING_FAILED", "COMPLETED", "FAILED", "REPORT_NOT_EXISTS", "NO_DATA", "COMPLETION"), #"NO_DATA", "COMPLETION" statuses not in doc but in api response
                            Optional("descripton"): And(str, lambda s: len(s) > 1),
                            Optional("report_urls"): And(str, lambda s: len(s) > 1),
                            "report_type": Or("BY_USER", "BY_CARRIER",  "BY_ALL_DEVICES", "BY_ALL_USERS", "BY_USER_ID", "BY_DEVICE_ID"),
                            "created_time": And(int, lambda s: len(str(s)) >= 5),
                            "carrier": testData.data["carrier"],
                            "start_time": And(int, lambda s: len(str(s)) >= 1),
                            "end_time": And(int, lambda s: len(str(s)) >= 1),
                            "result": "OK",
                            }
                        ]
                    }
        assert schema(api_schema) == self.response.json()
        return self

    def validateNotAuthReq_Schema(self):
        login_schema = {
                        "result": "NOT_AUTHORIZED",
                        "error": "Unauthorized"
                        }

        assert schema(login_schema) == self.response.json()
        return self

    def validateJsonContents(self):
        return self

    def add_new_device_report(self, environmentConfigs, testData):
        self.device_Response = self.get_new_device_report(environmentConfigs=environmentConfigs, testData=testData).json()

    def add_new_user_report(self, environmentConfigs, testData):
        self.user_response = self.get_new_user_report(environmentConfigs=environmentConfigs, testData=testData).json()

    def add_new_devices_report(self, environmentConfigs, testData):
        self.devices_Response = self.get_new_devices_report(environmentConfigs=environmentConfigs, testData=testData).json()

    def add_new_sessionByUser_report(self, environmentConfigs, testData):
        self.sessionByUser_response = self.get_new_devices_report(environmentConfigs=environmentConfigs, testData=testData).json()

    def add_new_SessionByCarrier_report(self, environmentConfigs, testData):
        self.sessionByCarrier_response = self.get_new_devices_report(environmentConfigs=environmentConfigs, testData=testData).json()


    def validate_devices_report_data(self):
        contor = 0
        for report in self.response.json()["reports"]:
            if report["task_code"] in self.devices_Response["task_code"]:
                assert self.devices_Response["status"] == report["status"], f'Status = {self.devices_Response["status"]} should be equal to {report["status"]}'
                assert self.devices_Response["created_time"] == report["created_time"], f'created_time = {self.devices_Response["created_time"]} should be equal to {report["created_time"]}'
                assert self.devices_Response["task_code"] == report["task_code"], f'task_code = {self.devices_Response["task_code"]} should be equal to {report["task_code"]}'
                contor += 1

        if contor == 0:
            assert False, "reports task code not found in response"

        return self

    def validate_user_report_data(self):
        contor = 0
        for report in self.response.json()["reports"]:
            if report["task_code"] in self.user_response["task_code"]:
                assert self.user_response["status"] == report["status"], f'Status = {self.user_response["status"]} should be equal to {report["status"]}'
                assert self.user_response["created_time"] == report["created_time"], f'created_time = {self.user_response["created_time"]} should be equal to {report["created_time"]}'
                assert self.user_response["task_code"] == report["task_code"], f'task_code = {self.user_response["task_code"]} should be equal to {report["task_code"]}'
                contor += 1

        if contor == 0:
            assert False, "reports task code not found in response"

        return self

    def validate_device_report_data(self):
        contor = 0
        for report in self.response.json()["reports"]:
            if report["task_code"] in self.device_Response["task_code"]:
                assert self.device_Response["status"] == report["status"], f'Status = {self.device_Response["status"]} should be equal to {report["status"]}'
                assert self.device_Response["created_time"] == report["created_time"], f'created_time = {self.device_Response["created_time"]} should be equal to {report["created_time"]}'
                assert self.device_Response["task_code"] == report["task_code"], f'task_code = {self.device_Response["task_code"]} should be equal to {report["task_code"]}'
                contor += 1

        if contor == 0:
            assert False, "reports task code not found in response"

        return self

    def validate_sessionByCarrier_report_data(self):
        contor = 0
        for report in self.response.json()["reports"]:
            if report["task_code"] in self.sessionByCarrier_response["task_code"]:
                assert self.sessionByCarrier_response["status"] == report["status"], f'Status = {self.sessionByCarrier_response["status"]} should be equal to {report["status"]}'
                assert self.sessionByCarrier_response["created_time"] == report["created_time"], f'created_time = {self.sessionByCarrier_response["created_time"]} should be equal to {report["created_time"]}'
                assert self.sessionByCarrier_response["task_code"] == report["task_code"], f'task_code = {self.sessionByCarrier_response["task_code"]} should be equal to {report["task_code"]}'
                contor += 1

        if contor == 0:
            assert False, "reports task code not found in response"

        return self

    def validate_sessionByUser_report_data(self):
        contor = 0
        for report in self.response.json()["reports"]:
            if report["task_code"] in self.sessionByUser_response["task_code"]:
                assert self.sessionByUser_response["status"] == report["status"], f'Status = {self.sessionByUser_response["status"]} should be equal to {report["status"]}'
                assert self.sessionByUser_response["created_time"] == report["created_time"], f'created_time = {self.sessionByUser_response["created_time"]} should be equal to {report["created_time"]}'
                assert self.sessionByUser_response["task_code"] == report["task_code"], f'task_code = {self.sessionByUser_response["task_code"]} should be equal to {report["task_code"]}'
                contor += 1

        if contor == 0:
            assert False, "reports task code not found in response"

        return self