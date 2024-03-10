from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.CSS_SELECTOR, "input[type='password']")
    checkbox = (By.CSS_SELECTOR, "input[type='checkbox']")
    dropdown = (By.XPATH, "//select[@class='form-control']/option[2]")
    empstatus = (By.CSS_SELECTOR, "#inlineRadio2")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    text1 = (By.CSS_SELECTOR, ".alert-dismissible")

    def ShopItems(self):
        return self.driver.find_element(*HomePage.shop)
        #driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")    shown for above line
    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getdropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def getempstatus(self):
        return self.driver.find_element(*HomePage.empstatus)

    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def gettext1(self):
        return self.driver.find_element(*HomePage.text1)
