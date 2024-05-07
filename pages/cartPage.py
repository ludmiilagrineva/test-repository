from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def moveToTheCartPage(self, wd):
        wd.find_element(By.XPATH, "//div[@id=\"cart\"]/a[@class=\"link\"]").click()

    def isCartEmpty(self, wd):
        if len(wd.find_elements(By.XPATH, "//div[@id=\"order_confirmation-wrapper\"]")) > 0:
            return False
        else:
            return True

    def removeProduct(self, wd):
        loc = wd.find_element(By.XPATH, "//button[@name=\"remove_cart_item\"]")
        loc.click()
        WebDriverWait(wd, 10).until((EC.staleness_of(loc)))

