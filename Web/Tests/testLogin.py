
from Utils.utils import Utils

import allure

from Pages.LoginPage import LoginPage
from Base.base import Base
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('set_up')
class TestLogin(Base):

    # __user_data_file = r"\login_details.xlsx"
    # df = pd.read_excel(os.getcwd() + __user_data_file)

    def test_login_success(self):
        driver = self.driver
        a = Utils(driver)
        login = LoginPage(driver)
        login.enter_email('miki')
        login.enter_password('12345')
        login.click_login()
        a.validtion("TripYoetz",driver.title,"pic")







    def test_login_unsuccess(self):
        driver = self.driver
        a = Utils(driver)
        login = LoginPage(driver)
        login.enter_email('mik')
        login.enter_password('12')
        login.click_login()
        a.validtion("Please include an '@' in the email address. 'mik' is missing an '@'.",login.get_err_message(),"pic")







