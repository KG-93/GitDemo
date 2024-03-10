from selenium import webdriver
from selenium.webdriver.chrome import service

service_obj = service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://google.co.im")
