import requests
from pytest_schema import schema, And, Optional
from BaseClass.Frontend.BaseAPIClass import BaseFacadeClass


class Partner_Report_SessionByCarrier_Facade(BaseFacadeClass):
    response = None

    def __init__(self):
        pass

    def executeSuccessfulRequest(self, environmentConfigs, testData):
        url = environmentConfigs.partner_ReportSessionByCarrier_URL

        headers = {
            "Authorization": f"Bearer {self.getAccessToken(environmentConfigs=environmentConfigs, testData=testData)}",
        }

        params = {
            "start_time": self.get_Start_endDate_ActiveSessions(environmentConfigs, testData)[0],
            "end_time": self.get_Start_endDate_ActiveSessions(environmentConfigs, testData)[0] + 1000,
            "tz": testData.data["tz"]
        }

        self.response = requests.post(url=url, params=params, headers=headers)
        self.pretty_print_POST(self.response.request)
        print(self.response.json())
        return self

    def executeNotAuthRequest(self, environmentConfigs, testData):
        url = environmentConfigs.partner_ReportSessionByCarrier_URL

        headers = {
            "Authorization": f"Bearer srewwq332",
        }

        params = {
            "start_time": self.get_Start_endDate_ActiveSessions(environmentConfigs, testData)[0],
            "end_time": self.get_Start_endDate_ActiveSessions(environmentConfigs, testData)[0] + 1000,
            "tz": testData.data["tz"]
        }

        self.response = requests.post(url=url, params=params, headers=headers)
        self.pretty_print_POST(self.response.request)
        print(self.response.json())
        return self

    def execute_invalid_tz_request(self, environmentConfigs, testData):
        url = environmentConfigs.partner_ReportDevices_URL

        headers = {
            "Authorization": f"Bearer {self.getAccessToken(environmentConfigs=environmentConfigs, testData=testData)}",
        }

        params = {
            "start_time": self.get_Start_endDate_ActiveSessions(environmentConfigs, testData)[0],
            "end_time": self.get_Start_endDate_ActiveSessions(environmentConfigs, testData)[0] + 1000,
            "tz": "notTz"
        }

        self.response = requests.post(url=url, params=params, headers=headers)
        self.pretty_print_POST(self.response.request)
        print(self.response.json())
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

    def validateSuccessfulReq_Schema(self):

        """{
result: enum
Allowed: OK┃NOT_FOUND┃INVALID_PARAMS
error: string
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

Allowed: NEW┃QUERYING┃QUERYING_FAILED┃EXPORTING┃EXPORTING_FAILED┃COMPLETION┃COMPLETED┃FAILED┃REPORT_NOT_EXISTS┃NO_DATA
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
}"""
        api_schema = {
                        "result": "OK",
                        "task_code": And(str, lambda s: len(s) > 1),
                        "status": "NEW",
                        Optional("description"): And(str, lambda s:len(s) > 1),
                        Optional("report_urls"): And(str, lambda s: len(s) > 1),
                        "report_type": "BY_CARRIER",
                        "created_time": And(int, lambda s: len(str(s)) >= 5),
                        Optional("carrier"): And(str, lambda s: len(s) > 1),
                        Optional("start_time"): And(int, lambda s: len(str(s)) >= 5),
                        Optional("end_time"): And(int, lambda s: len(str(s)) >= 5),
        }

        assert schema(api_schema) == self.response.json()
        return self

    def validateNotAuthReq_Schema(self):
        login_schema = {
                        "result": "NOT_AUTHORIZED",
                        }

        assert schema(login_schema) == self.response.json()
        return self

    def validateJsonContents(self):
        pass



# if __name__ == "__main__":
#     currentAPi = User_Current_API_Facade()
#     currentAPi.getRequest_user_current_API()
#     currentAPi.validateSuccessfullStatusCode()
#     currentAPi.validateJsonContents()
