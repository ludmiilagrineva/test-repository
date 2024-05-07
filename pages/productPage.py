from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def isFindedElementSize(self, wd):
        elements = wd.find_elements(By.XPATH, "//select[@name=\"options[Size]\"]")
        if len(elements) > 0:
            return True
        else:
            return False

    def selectSizeDucks(self, wd):
        selectSize = wd.find_element(By.XPATH, "//select[@name=\"options[Size]\"]")
        wd.execute_script("arguments[0].selectedIndex=2; arguments[0].dispatchEvent(new Event('change'))", selectSize)

    def addProduct(self, wd):
        wd.find_element(By.XPATH, "//button[@name=\"add_cart_product\"]").click()

    def waitAddedToTheCart(self, wd, i):
        WebDriverWait(wd, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//span[@class=\"quantity\"]"), str(i)))
        wd.find_element(By.XPATH, "//div[@id=\"logotype-wrapper\"]").click()