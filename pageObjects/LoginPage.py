from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By


class LoginPage(BaseClass):
    email_textbox = (By.XPATH, "//input[@name='email']")
    password_textbox = (By.XPATH, "//input[@name='password']")
    login_button = (By.XPATH, "//input[@type='submit' and @value='Login']")
    my_account_verify_login = (By.XPATH, "//h2[text()='My Account']")

    def __init__(self, driver):
        self.driver = driver

    def type_email(self, email_address):
        self.wait_for_element_to_be_visible(self.email_textbox).send_keys(email_address)

    def type_password(self, password_text):
        self.wait_for_element_to_be_visible(self.password_textbox).send_keys(password_text)

    def click_login_button(self):
        self.wait_for_element_to_be_visible(self.login_button).click()

    def is_account_exists(self):
        try:
            my_account_text = self.wait_for_element_to_be_visible(self.my_account_verify_login)
            return my_account_text.is_displayed()
        except:
            return False
