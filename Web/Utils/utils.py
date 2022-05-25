import allure
from Base.base import Base
from selenium import webdriver


class Utils():
    def __init__(self,driver):
        self.driver = driver

    def validtion(self,expected, actual,pic):
        driver = self.driver
        try:
            assert expected == actual
        except Exception:
            allure.attach(driver.get_screenshot_as_png(), driver.save_screenshot(pic),
                          attachment_type=allure.attachment_type.PNG)




