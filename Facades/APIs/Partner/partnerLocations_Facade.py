import requests
from pytest_schema import schema, And
from BaseClass.Frontend.BaseAPIClass import BaseFacadeClass


class Partner_Locations_Facade(BaseFacadeClass):
    response = None

    def __init__(self):
        pass

    def execute_Successful_Req_with_public_server_pool(self, environmentConfigs, testData):
        url = environmentConfigs.partner_Locations_URL
        headers = {
            "Authorization": f"Bearer {self.getAccessToken(environmentConfigs=environmentConfigs, testData=testData)}",

        }
        params = {
            "protocol": testData.data["protocol"],
            "server_pool": testData.data["public_server_pool"],}
        self.response = requests.get(url=url, headers=headers, params=params)
        print(self.response.json())
        return self

    def execute_Successful_Req_with_private_server_pool(self, environmentConfigs, testData):
        url = environmentConfigs.partner_Locations_URL
        headers = {
            "Authorization": f"Bearer {self.getAccessToken(environmentConfigs=environmentConfigs, testData=testData)}",

        }
        params = {
            "protocol": testData.data["protocol"],
            "server_pool": testData.data["private_server_pool"],}
        self.response = requests.get(url=url, headers=headers, params=params)
        self.pretty_print_POST(self.response.request)
        print(self.response.json())
        return self

    def execute_Successful_Req_with_free_user_status(self, environmentConfigs, testData):
        url = environmentConfigs.partner_Locations_URL
        headers = {
            "Authorization": f"Bearer {self.getAccessToken(environmentConfigs=environmentConfigs, testData=testData)}",

        }
        params = {
            "protocol": testData.data["protocol"],
            "user_status": "free"}
        self.response = requests.get(url=url, headers=headers, params=params)
        print(self.response.json())
        return self


    def execute_Successful_Req_with_paid_user_status(self, environmentConfigs, testData):
        url = environmentConfigs.partner_Locations_URL
        headers = {
            "Authorization": f"Bearer {self.getAccessToken(environmentConfigs=environmentConfigs, testData=testData)}",

        }
        params = {
            "protocol": testData.data["protocol"],
            "user_status": "paid"}
        self.response = requests.get(url=url, headers=headers, params=params)
        print(self.response.json())
        return self

    def execute_negative_request_with__both_serverPool_and_userStatus(self, environmentConfigs, testData):
        url = environmentConfigs.partner_Locations_URL
        headers = {
            "Authorization": f"Bearer {self.getAccessToken(environmentConfigs=environmentConfigs, testData=testData)}",
        }
        params = {
            "protocol": testData.data["protocol"],
            "server_pool": testData.data["private_server_pool"],
            "user_status": "paid"}
        self.response = requests.get(url=url, headers=headers, params=params)
        print(self.response.json())
        return self


    def executeNotAuthRequest(self, environmentConfigs, testData):
        url = environmentConfigs.partner_Locations_URL
        headers = {
            "Authorization": f"Bearer False",

        }
        params = {
            "protocol": testData.data["protocol"],
            "server_pool": testData.data["public_server_pool"],}
        self.response = requests.get(url=url, headers=headers, params=params)
        print(self.response.json())
        return self

    def validate_200_StatusCode(self):
        assert self.response.status_code == 200, f"Status code should be 200 'OK' but got status code = '{self.response.status_code}'"
        return self

    def validate_400_StatusCode(self):
        assert self.response.status_code == 401, f"Status code should be 401 'NOT_AUTHORIZED' but got status code = '{self.response.status_code}'"
        return self

    def validateSuccessfulReq_Schema(self):
        """{
result: enum

locations: [{
name: string
description: string
labels: {
<any-key>: string
}
status: string
}]}"""

        api_schema = {
            "result": "OK",
            "locations": [{
                "name": And(str, lambda s: len(s) > 1),
                "description": And(str, lambda s: len(s) >= 1),
                "labels": {
                    "subdivision": str,
                    "country": And(str, lambda s: len(s) >= 1),
                    "city": And(str, lambda s: len(s) >= 1),
                },
                "status": And(str, lambda s: len(s) >= 1),
            }]
        }

        assert schema(api_schema) == self.response.json()
        return self

    def validateNotAuthReq_Schema(self):
        license_schema = {
                        "result": "NOT_AUTHORIZED",
                        }

        assert schema(license_schema) == self.response.json()

        return self

    def validateNegativeRequest_with_both_params_provided_Schema(self):
        license_schema = {
                        "result": "NOT_AUTHORIZED",
                        "error": "only one of parameters server_pool or user_status should be set"
                        }

        assert schema(license_schema) == self.response.json()

        return self

    def validateJsonContents(self):
        pass

