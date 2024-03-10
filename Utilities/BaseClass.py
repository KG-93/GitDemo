import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("test_invokebrowser")
class BaseClass:

    def VerifyLinkText(self, text):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)
        return logger
