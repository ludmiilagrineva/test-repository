from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.mainUrl = ("http://localhost/litecart/en/")
        self.wait = WebDriverWait(driver, 10)

    def moveToTheMainPage(self):
        return self.driver.get(self.mainUrl)

    def moveToTheProductToCart(self, wd, num):
        wd.find_element(By.XPATH, f"//div[@id=\"box-most-popular\"]/div/ul/li[{num}]/a").click()
