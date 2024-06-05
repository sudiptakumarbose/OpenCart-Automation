from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass
import os
from utilities.readProperties import ReadConfig

class Homepage(BaseClass):
    my_account_link = (By.XPATH, "//span[text()='My Account']")
    register_link = (By.LINK_TEXT, "Register")
    login_link = (By.LINK_TEXT, "Login")

    def __init__(self, driver):
        self.driver = driver

    def launch_url(self):
        url = ReadConfig.getApplicationURL()
        self.driver.get(url)
        self.driver.maximize_window()

    def click_on_my_account_button(self):
        self.wait_for_element_to_be_clickable(self.my_account_link).click()

    def click_on_register_button(self):
        self.wait_for_element_to_be_clickable(self.register_link).click()

    def click_on_login_button(self):
        self.wait_for_element_to_be_clickable(self.login_link).click()

    def save_screenshots(self):
        screenshot_path = os.path.join(os.path.abspath(os.curdir), "screenshots", "test_account_registration.png")
        return self.driver.save_screenshot(screenshot_path)
