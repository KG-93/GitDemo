from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    checkoutconfirm = (By.XPATH, "//button[@class='btn btn-success']")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitt = (By.XPATH, "//input[@type='submit']")
    textt = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def checkout(self):
        return self.driver.find_element(*ConfirmPage.checkoutconfirm)

    def checkboxx(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def submit(self):
        return self.driver.find_element(*ConfirmPage.submitt)

    def alerttext(self):
        return self.driver.find_element(*ConfirmPage.textt)
