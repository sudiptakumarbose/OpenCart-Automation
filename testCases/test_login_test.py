import pytest
from pageObjects.HomePage import Homepage
from pageObjects.Account_registration_Page import AccountRegistration
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.BaseClass import BaseClass


class Test_Login(BaseClass):
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login(self):
        HomePage = Homepage(self.driver)
        Loginpage = LoginPage(self.driver)
        HomePage.launch_url()
        self.logger.info("--Launching Login Test URL---")
        HomePage.click_on_my_account_button()
        self.logger.info("--Clicking on My Account Button---")

        HomePage.click_on_login_button()
        self.logger.info("--Clicking on Login Button---")

        Loginpage.type_email("q3jch@gmail.com")
        self.logger.info("--Typing the email address---")

        Loginpage.type_password("Abcdef12")
        self.logger.info("--Typing the password---")
        Loginpage.click_login_button()
        self.logger.info("--Clicking the login button---")
        verification_page = Loginpage.is_account_exists()
        if verification_page == True:
            self.logger.info("---LoginTest passed---")
            self.driver.close()
            assert True
        else:
            self.take_screenshot("test_login")
            self.logger.info("---LoginTest Failed---")
            self.driver.close()
            assert False
