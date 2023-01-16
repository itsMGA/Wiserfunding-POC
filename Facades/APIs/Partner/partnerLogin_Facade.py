import requests
from pytest_schema import schema, And
from BaseClass.Frontend.BaseAPIClass import BaseFacadeClass


class Partner_Login_Facade(BaseFacadeClass):
    response = None

    def __init__(self):
        pass

    def executeSuccessfulRequest(self, environmentConfigs, testData):
        url = environmentConfigs.partner_Login_POST_URL
        headers = {
            "login": testData.data["username"],
            "password": testData.data["password"]
        }
        self.response = requests.post(url=url, params=headers)
        self.pretty_print_POST(self.response.request)
        print(self.response.json())
        self.setTempData("access_token", self.response.json()["access_token"])
        return self

    def executeNotAuthRequest(self, environmentConfigs, testData):
        url = environmentConfigs.partner_Login_POST_URL
        headers = {
            "login": testData.data["username"],
            "password": "randomPassowrd"
        }
        self.response = requests.post(url=url, params=headers)
        self.pretty_print_POST(self.response.request)
        print(self.response.json())
        return self

    def validate_200_StatusCode(self):
        assert self.response.status_code == 200, f"Status code should be 200 'OK' but got status code = '{self.response.status_code}'"
        return self


    def validateSuccessfulReq_Schema(self):
        login_schema = {
                        "result": "OK",
                        "access_token": And(str, lambda s: len(s) > 2),
                        "create_time": And(int, lambda s: len(str(s)) >= 10),
                        "expire_time": And(int, lambda s: len(str(s)) >= 10),
                        }

        assert schema(login_schema) == self.response.json()
        return self

    def validateNotAuthReq_Schema(self):
        login_schema = {
                        "result": "NOT_AUTHORIZED",
                        "error": "invalid login or password"
                        }

        assert schema(login_schema) == self.response.json()
        return self

    def validateNotAuthReq_Schema(self):
        login_schema = {
                        "result": "NOT_AUTHORIZED",
                        "error": "invalid login or password"
                        }

        assert schema(login_schema) == self.response.json()
        return self

    def validateNotAuthReq_Schema(self):
        login_schema = {
                        "result": "NOT_AUTHORIZED",
                        "error": "invalid login or password"
                        }

        assert schema(login_schema) == self.response.json()
        return self

    def validateNotAuthReq_Schema(self):
        login_schema = {
                        "result": "NOT_AUTHORIZED",
                        "error": "invalid login or password"
                        }

        assert schema(login_schema) == self.response.json()
        return self

    def validateNotAuthReq_Schema(self):
        login_schema = {
                        "result": "NOT_AUTHORIZED",
                        "error": "invalid login or password"
                        }

        assert schema(login_schema) == self.response.json()
        return self

    def validateNotAuthReq_Schema(self):
        login_schema = {
                        "result": "NOT_AUTHORIZED",
                        "error": "invalid login or password"
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
