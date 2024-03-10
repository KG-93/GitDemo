from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardtitle = (By.XPATH, "//div[@class='card h-100']")
    checkoutbutton = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")

    def getcardtitles(self):
        return self.driver.find_elements(*CheckOutPage.cardtitle)

    def checkoutbuttonn(self):
        self.driver.find_element(*CheckOutPage.checkoutbutton).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
