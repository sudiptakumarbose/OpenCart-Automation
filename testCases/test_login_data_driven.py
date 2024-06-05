from pageObjects.HomePage import Homepage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccount import MyAccountPage
from utilities.BaseClass import BaseClass
from utilities.customLogger import LogGen
from utilities import ExcelUtils


class Test_login_data_driven(BaseClass):
    logger = LogGen.loggen()
    path = "C:\\Users\\AB\\PycharmProjects\\OpenCart_automation\\testdata\\Opencart_LoginData.xlsx"

    def test_login_data_driven(self):
        rows = ExcelUtils.getRowCount(self.path, "Sheet1")
        print(rows)
        status = []
        HomePage = Homepage(self.driver)
        Loginpage = LoginPage(self.driver)
        MyAccount = MyAccountPage(self.driver)
        HomePage.launch_url()
        self.logger.info("--Launching Login Test URL---")
        for i in range(2, rows + 1):
            HomePage.click_on_my_account_button()
            self.logger.info("--Clicking on My Account Button---")
            HomePage.click_on_login_button()
            self.logger.info("--Clicking on Login Button---")
            email_address = ExcelUtils.readData(self.path, "Sheet1", i, 1)
            password = ExcelUtils.readData(self.path, "Sheet1", i, 2)
            expected_result = ExcelUtils.readData(self.path, "Sheet1", i, 3)
            Loginpage.type_email(email_address)
            self.logger.info("---Typing the email address---")
            Loginpage.type_password(password)
            self.logger.info("---Typing the password---")
            Loginpage.click_login_button()
            verification_page = Loginpage.is_account_exists()
            if expected_result == "Valid":
                if verification_page == True:
                    status.append("Pass")
                    MyAccount.click_logout()
                    self.logger.info("---LoginTest passed---")
                else:
                    status.append("Fail")
                    MyAccount.click_logout()
            elif expected_result == "Invalid":
                if verification_page == True:
                    status.append("Fail")
                    MyAccount.click_logout()
                else:
                    status.append("Pass")
        self.driver.close()
        if "Fail" not in status:
            assert True
        else:
            assert False
