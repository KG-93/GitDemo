import time
import pytest

from TestData import HomePageData
from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class homePage(BaseClass):


    def test_homepage1(self, logindata):

        log = self.getlogger()
        homepagee = HomePage(self.driver)
        homepagee.getname()
        homepagee.getname().send_keys(logindata["firstname"])  # name
        log.info(logindata["firstname"])
        homepagee.getemail().send_keys(logindata["lastname"])  # email
        homepagee.getpassword().send_keys("12345")  # password field
        homepagee.getcheckbox().click()  # checkbox
        homepagee.getdropdown().click()  # dropdown gender
        homepagee.getempstatus().click()  # employment status
        homepagee.getsubmit().click()  # Submit button

        text = homepagee.gettext1().text  # alert text
        print(text)
        log.info(text)
        assert "successs" in text

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.gettestdata("testcase1"))
    def logindata(self, request):
        return request.param

    time.sleep(5)
