import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

@pytest.mark.usefixtures("setup")
class BaseClass:

    def wait_for_element_to_be_visible(self, text):
        try:
            element = WebDriverWait(self.driver, 160).until(EC.visibility_of_element_located(text))
            return element
        except TimeoutException:
            return None

    def wait_for_element_to_be_clickable(self, locator):
        try:
            element = WebDriverWait(self.driver, 160).until(EC.element_to_be_clickable(locator))
            return element
        except TimeoutException:
            None

    def take_screenshot(self, file_name):

        screenshots_dir = "C:\\Users\\AB\\PycharmProjects\\OpenCart_automation\\screenshots\\"

        # Construct the filename with a timestamp
        filename = f"{file_name}.png"

        # Combine path and filename
        filepath = os.path.join(screenshots_dir, filename)

        # Save the screenshot using the absolute path
        self.driver.save_screenshot(filepath)
