import pytest

from selenium import webdriver


class Base:
    # def __init__(self):
    #     self.driver_path = 'C:/Users/Mikin/PycharmProjects/test_with_class/Drivers/chromedriver.exe'

    @pytest.fixture(autouse=True)
    def set_up(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome(executable_path='C:/Users/Mikin/PycharmProjects/test_with_class/Drivers/chromedriver.exe')
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get("https://trip-yoetz.herokuapp.com/login")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()