import time
import allure
import pytest
from selenium.webdriver.common.keys import Keys

from Locators.Home_Locators import HomeLocators
from selenium.webdriver.common.by import By
from time import sleep


class HomePage:

    def __init__(self,driver):
        self.driver = driver
        self.nav_bar_path = HomeLocators.nav_bar_path
        # self.register_path = HomeLocators.register_path
        # self.about_path = HomeLocators.about_path
        # self.home_path = HomeLocators
        self.search_in_navbar_path = HomeLocators.search_in_navbar_path
        self.discoverParis_path = HomeLocators.discoverParis_path

#clicking nav bar in loop
    def enter_nuvbar(self):
        nav_bar = self.driver.find_elements(By.XPATH, self.nav_bar_path)
        for i in range(len(nav_bar)):
            nav_bar[i].click()
            self.driver.back()

#clicking bav bar without loop

    #     self.driver.find_element(By.XPATH,self.login_path).click()
    #     self.driver.find_element(By.XPATH, self.login_path).get_attribute("innerText")
    #     self.driver.back()
    #     self.driver.find_element(By.XPATH,self.register_path).click()
    #     sleep(3)
    #     self.driver.back()
    #     sleep(3)
    #     self.driver.find_element(By.XPATH,self.about_path).click()
    #     self.driver.back()
    @pytest.mark.usefixtures('set_up')
    def search_correct(self,city):
        self.driver.find_element(By.XPATH, self.search_in_navbar_path).send_keys(city)
        self.driver.find_element(By.XPATH, self.search_in_navbar_path).send_keys(Keys.ENTER)

    def discoverParis_msg(self):
        return self.driver.find_element(By.XPATH, self.discoverParis_path).get_attribute("innerText")









































