from Pages.Settings_Page import Settings_Page

class SettingsPage_Facade:

    def __init__(self, page, testData, environmentConfigs):
        self.page = page
        self.testData = testData
        self.environmentConfigs = environmentConfigs
        self.settings_page = Settings_Page(self.page, self.testData, self.environmentConfigs)

    def change_password(self):
        self.settings_page.settings_button.click()
        self.settings_page.current_pass_input.type(self.testData.data["password"])
        self.settings_page.new_pass.type(self.testData.data["new_pass"])
        self.settings_page.confirm_new_pass.type(self.testData.data["new_pass"])
        self.settings_page.save_btn.click()
        assert self.settings_page.succesfully_changed_password_notif.is_enabled(), "Changed password did not work!"