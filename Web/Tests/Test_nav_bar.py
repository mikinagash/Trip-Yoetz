from Web.Pages.Home_page import HomePage
from Web.Base.base import Base
import pytest


@pytest.mark.usefixtures('set_up')
class TestNavBar(Base):
    @pytest.mark.nightly

    def test_nav_bar_loop(self):
        driver = self.driver
        home = HomePage(driver)
        home.enter_nuvbar()



    def test_search_nav_bar(self):
        driver = self.driver
        home = HomePage(driver)
        home.search_correct("paris")
        assert "Discover Paris" == home.discoverParis_msg()








