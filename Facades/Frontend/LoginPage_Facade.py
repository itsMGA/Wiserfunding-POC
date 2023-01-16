from Pages.Login_Page import LoginPage


class LoginPage_Facade:

    def __init__(self, page, testData, environmentConfigs):
        self.page = page
        self.testData = testData
        self.environmentConfigs = environmentConfigs
        self.login_page = LoginPage(testData=self.testData, environmentConfigs=self.environmentConfigs, context=self.page)

    def succesful_login(self):
        self.login_page.username_input.type(self.testData.data['username'])
        self.login_page.password_input.type(self.testData.data['password'])
        self.login_page.singIn_button.click()
        assert self.login_page.welcome_back_header.text_content() == "Welcome back,", "Dashboard Welcome back header missing!"