import pytest

from selenium import webdriver


class Base:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/Mikin/PycharmProjects/test_with_class/Drivers/chromedriver.exe')
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get("https://trip-yoetz.herokuapp.com/login")
        self.driver.maximize_window()



