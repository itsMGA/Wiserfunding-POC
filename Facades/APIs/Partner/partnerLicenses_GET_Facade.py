import requests
from pytest_schema import schema, And
from BaseClass.Frontend.BaseAPIClass import BaseFacadeClass


class Partner_Licenses_Facade(BaseFacadeClass):
    response = None

    def __init__(self):
        pass

    def executeSuccessfulRequest(self, environmentConfigs, testData):
        url = environmentConfigs.partner_Licenses_GET_URL
        headers = {
            "Authorization": f"Bearer {self.getAccessToken(environmentConfigs=environmentConfigs, testData=testData)}",
        }
        self.response = requests.get(url=url, headers=headers)
        print(self.response.json())
        return self

    def executeNotAuthRequest(self, environmentConfigs, testData):
        url = environmentConfigs.partner_Licenses_GET_URL
        headers = {
            "Authorization": "Bearer e4do0pd19q4brca21euuewq732ek321wqeq0c3df5vha58828mmecr",
        }
        self.response = requests.get(url=url, headers=headers)
        self.pretty_print_POST(self.response.request)
        print(self.response.json())
        return self

    def validate_200_StatusCode(self):
        assert self.response.status_code == 200, f"Status code should be 200 'OK' but got status code = '{self.response.status_code}'"
        return self

    def validate_400_StatusCode(self):
        assert self.response.status_code == 401, f"Status code should be 401 'NOT_AUTHORIZED' but got status code = '{self.response.status_code}'"
        return self

    def validateSuccessfulReq_Schema(self):
        license_schema = {

            "licenses":
                                    [{
                                    "id": And(int, lambda id: id >= 1),
                                    "name": str,
                                    "devices_limit": int,
                                    "sessions_limit": int
                                    }],
            "result": "OK"
                        }

        assert schema(license_schema) == self.response.json()
        return self

    def validateNotAuthReq_Schema(self):
        license_schema = {
                        "result": "NOT_AUTHORIZED",
                        }

        assert schema(license_schema) == self.response.json()
        return self

    def validateJsonContents(self):
        pass
