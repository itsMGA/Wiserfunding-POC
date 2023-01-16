import requests
from pytest_schema import schema
from BaseClass.Frontend.BaseAPIClass import BaseFacadeClass


class Partner_FilesUpload_Facade(BaseFacadeClass):
    response = None

    def __init__(self):
        pass

    def executeSuccessfulRequest(self, environmentConfigs, testData):
        url = environmentConfigs.partner_filesUpload_URL
        headers = {
            "Authorization": f"Bearer {self.getAccessToken(environmentConfigs=environmentConfigs, testData=testData)}"
        }
        params = {
            "publickey": testData.data["project_name"],
            "name": "testFile"
                }

        testFilePath = f"{self.get_project_root()}/TestData/testFiles/bpl.txt"
        with open(testFilePath, mode="rb") as testFile:
            body = {"file": testFile}
            self.response = requests.post(url=url, params=params, headers=headers, files=body)

        self.pretty_print_POST(self.response.request)
        print(self.response.json())
        return self

    def executeNotAuthRequest(self, environmentConfigs, testData):
        url = environmentConfigs.partner_filesUpload_URL
        headers = {
            "Authorization": f"Bearer Aewqe12qweasd"
        }
        params = {
            "publickey": testData.data["project_name"],
            "name": "testFile"
                }

        testFilePath = f"{self.get_project_root()}/TestData/testFiles/bpl.txt"
        with open(testFilePath, mode="rb") as testFile:
            body = {"file": testFile}
            self.response = requests.post(url=url, params=params, headers=headers, files=body)

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
        login_schema = {
                        "result": "OK",
                        }

        assert schema(login_schema) == self.response.json()
        return self

    def validateNotAuthReq_Schema(self):
        login_schema = {
                        "result": "NOT_AUTHORIZED",
                        }

        assert schema(login_schema) == self.response.json()
        return self

    def validateJsonContents(self):
        pass

    def executeSuccesfull_wEmptyStringValues(self, environmentConfigs, testData):
        url = environmentConfigs.partner_filesUpload_URL
        headers = {
            "Authorization": f"Bearer {self.getAccessToken(environmentConfigs=environmentConfigs, testData=testData)}"
        }
        params = {
            "publickey": " ",
            "name": " "
                }

        testFilePath = f"{self.get_project_root()}/TestData/testFiles/bpl.txt"
        with open(testFilePath, mode="rb") as testFile:
            body = {"file": testFile}
            self.response = requests.post(url=url, params=params, headers=headers, files=body)

        self.pretty_print_POST(self.response.request)
        print(self.response.json())
        return self


# if __name__ == "__main__":
#     currentAPi = User_Current_API_Facade()
#     currentAPi.getRequest_user_current_API()
#     currentAPi.validateSuccessfullStatusCode()
#     currentAPi.validateJsonContents()
