from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By


class AccountRegistration(BaseClass):
    first_name = (By.NAME, "firstname")
    last_name = (By.NAME, "lastname")
    email = (By.NAME, "email")
    telephone = (By.NAME, "telephone")
    password = (By.NAME, "password")
    confirm_password = (By.NAME, "confirm")
    privacy_policy = (By.XPATH, "//input[@type='checkbox' and @name='agree']")
    continue_button = (By.XPATH, "//input[@value='Continue']")
    text_message_confirmation=(By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']")

    def __init__(self, driver):
        self.driver = driver

    def type_first_name(self, f_name):
        self.wait_for_element_to_be_visible(self.first_name).send_keys(f_name)

    def type_last_name(self, l_name):
        self.wait_for_element_to_be_visible(self.last_name).send_keys(l_name)

    def type_email(self, email_address):
        self.wait_for_element_to_be_visible(self.email).send_keys(email_address)

    def type_telephone(self, mobile):
        self.wait_for_element_to_be_visible(self.telephone).send_keys(mobile)

    def type_password(self, passw):
        self.wait_for_element_to_be_visible(self.password).send_keys(passw)

    def confirm_pass(self, confirm_pwd):
        self.wait_for_element_to_be_visible(self.confirm_password).send_keys(confirm_pwd)

    def handle_privacy_policy(self):
        self.wait_for_element_to_be_clickable(self.privacy_policy).click()

    def click_continue_button(self):
        self.wait_for_element_to_be_clickable(self.continue_button).click()

    def get_confirmation_message(self):
        try:
            confirmation_message=self.wait_for_element_to_be_visible(self.text_message_confirmation)
            confirmation_text=confirmation_message.text
            return confirmation_text
        except:
            None