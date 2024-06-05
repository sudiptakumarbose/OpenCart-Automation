from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class MyAccountPage(BaseClass):
    logout_button = (By.XPATH, "//aside[@id='column-right']//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        self.wait_for_element_to_be_clickable(self.logout_button).click()
