import pytest

from utilities import random_string
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import Homepage
from pageObjects.Account_registration_Page import AccountRegistration
import os
from utilities.customLogger import LogGen


class Testaccountregistration(BaseClass):
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_account_registration(self, setup):

        home_page = Homepage(self.driver)
        account_registration_page = AccountRegistration(self.driver)
        self.logger.info("---Account Registration Test---")
        home_page.launch_url()
        self.logger.info("---Launching Application Url---")
        home_page.click_on_my_account_button()
        home_page.click_on_register_button()
        self.logger.info("---Clicking on Register Button---")
        account_registration_page.type_first_name("Sudipta")
        account_registration_page.type_last_name("Bose")
        email = random_string.random_string_generator() + '@gmail.com'
        account_registration_page.type_email(email)
        self.logger.info("--Typing the email field--'%s'", email)
        account_registration_page.type_telephone("12345678")
        account_registration_page.type_password("Abcdef12")
        account_registration_page.confirm_pass("Abcdef12")
        account_registration_page.handle_privacy_policy()
        account_registration_page.click_continue_button()
        confirmation_message = account_registration_page.get_confirmation_message()
        if confirmation_message == "Your Account Has Been Created!":
            self.logger.info("---Account Registration successful---")
            self.driver.close()
            assert True
        else:
            self.take_screenshot("test_account_registration")
            self.logger.info("---Account Registration not successful---")
            self.driver.close()
            assert False

        self.logger.info("---Account Registration test finished---")

