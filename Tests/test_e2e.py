import time
from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    # def test_e2e(self):
    #
    #     list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
    #     list1 = []
    #
    #     self.driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
    #     time.sleep(3)
    #     product_names = self.driver.find_elements(By.XPATH, "//div[@class='products']/div")
    #     # product_names = driver.find_elements(By.CSS_SELECTOR, "h4.product-name")
    #     count = len(product_names)
    #     assert count > 0
    #     print(count)
    #     for product_name in product_names:
    #         list1.append(product_name.find_element(By.XPATH, "h4").text)
    #
    #     print(list)
    #     print(list1)
    #     assert list == list1
    #
    #     time.sleep(5)


    def test_e2e2(self):

        log = self.getlogger()
        card_title_list = []
        homepage = HomePage(self.driver)

        homepage.ShopItems().click()
        log.info("getting all the card titles")
        # self.driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
        self.driver.execute_script("window.scrollBy(0,550);")

        checkoutpage = CheckOutPage(self.driver)
        card_details = checkoutpage.getcardtitles()

        # card_details = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for card_detail in card_details:
            card_title_list.append(card_detail.find_element(By.XPATH, "div/h4").text)
            if "Blackberry" in card_title_list:
                card_detail.find_element(By.XPATH, "div/button").click()

        log.info(card_title_list)
        # print(card_title_list)
        self.driver.execute_script("window.scrollTo(0,50);")

        checkoutpage.checkoutbuttonn()
        # self.driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()

        confirmpage = ConfirmPage(self.driver)
        confirmpage.checkout().click()
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        log.info("entering country name as ind")
        self.driver.find_element(By.ID, "country").send_keys("in")

        self.VerifyLinkText("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()
        log.info("getting country name")
        print(self.driver.find_element(By.CSS_SELECTOR, "#country").get_attribute("value"))

        confirmpage.checkboxx().click()
        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirmpage.submit().click()
        # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        text = confirmpage.alerttext().text
        # text = self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
        print(text)
        # assert "suuccesss" in text
        # log.info("text recieved from the applicatiom is " + text)
        assert "Success!" in text
        log.info(text)
        time.sleep(6)
