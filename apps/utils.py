import json
import os
from pathlib import Path
from ast import literal_eval

class Ultilities:

    def __init__(self):
        self.localFile = rf"{self.get_project_root()}/secrets/testData.json"

    def getLocalData(self):
        if os.path.isfile(self.localFile):
            with open(self.localFile, mode="r", encoding='utf-8') as localFile:
                localFileJson = json.loads(localFile.read())
            return localFileJson
        else:
            return {"LocalData": "NotFound"}

    def shuffle_passwords(self):

        # Open the JSON file
        with open(self.localFile, "r") as json_file:
            data = literal_eval(json_file.read())

        # Swap the values of the "password" and "new_pass" keys
        data["password"], data["new_pass"] = data["new_pass"], data["password"]
        # Write the updated JSON data to the same file
        with open(self.localFile, "w") as json_file:
            json_file.write(json.dumps(data, indent=3))

    def get_project_root(self) -> Path:
        return Path(__file__).parent.parent

if __name__ == '__main__':
    utils = Ultilities()
    utils.shuffle_passwords()