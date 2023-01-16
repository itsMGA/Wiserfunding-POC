import requests
from pytest_schema import schema
from BaseClass.Frontend.BaseAPIClass import BaseFacadeClass


class Partner_ActiveSessions_Facade(BaseFacadeClass):
    response = None

    def __init__(self):
        pass

    def executeSuccessfulRequest(self, environmentConfigs, testData):
        url = environmentConfigs.partner_ActiveSessions_GET_URL
        headers = {
            "access_token": self.getAccessToken(environmentConfigs, testData)
        }

        self.response = requests.get(url=url, params=headers)
        self.pretty_print_POST(self.response.request)
        print(self.response.json())
        return self

    def executeNotAuthRequest(self, environmentConfigs, testData):
        url = environmentConfigs.partner_ActiveSessions_GET_URL
        headers = {
            "access_token": "random invalid token"
        }
        self.response = requests.get(url=url, params=headers)
        self.pretty_print_POST(self.response.request)
        print(self.response.json())
        return self

    def validate_200_StatusCode(self):
        assert self.response.status_code == 200, f"Status code should be 200 'OK' but got status code = '{self.response.status_code}'"
        return self

    def validate_401_StatusCode(self):
        assert self.response.status_code == 401, f"Status code should be 401 'NOT_AUTHORIZED' but got status code = '{self.response.status_code}'"
        return self


    def validateSuccessfulReq_Schema(self):

        yaml_schema = {
            "sessions":
                [{
                "user_id": int,
                "device_id": str,
                "server": str,
                "start_time": int,
                "end_time": int,
                "internal_address": str,
                "tx": int,
                "rx": int,
                "server_country": str
                    }],
            "result": "OK"
        }


        assert schema(yaml_schema) == self.response.json()
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
