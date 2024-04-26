import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

@pytest.fixture
def driver (request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def isFindedElementSize(wd):
    elements=wd.find_elements(By.XPATH, "//select[@name=\"options[Size]\"]")
    if len(elements)>0:
        return True
    else:
        return False

def addProductToCart(wd, num):
    wd.find_element(By.XPATH, f"//div[@id=\"box-most-popular\"]/div/ul/li[{num}]/a").click()
    if isFindedElementSize(wd):
        selectSize = wd.find_element(By.XPATH, "//select[@name=\"options[Size]\"]")
        wd.execute_script("arguments[0].selectedIndex=2; arguments[0].dispatchEvent(new Event('change'))", selectSize)
    wd.find_element(By.XPATH, "//button[@name=\"add_cart_product\"]").click()


def test_example(driver):
    driver.get("http://localhost/litecart/en/")
    for i in range(1, 4):
        addProductToCart(driver, i)
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//span[@class=\"quantity\"]"), str(i)))
        driver.find_element(By.XPATH, "//div[@id=\"logotype-wrapper\"]").click()

    driver.find_element(By.XPATH, "//div[@id=\"cart\"]/a[@class=\"link\"]").click()

    while len(driver.find_elements(By.XPATH, "//div[@id=\"order_confirmation-wrapper\"]"))>0:
        loc = driver.find_element(By.XPATH, "//button[@name=\"remove_cart_item\"]")
        loc.click()
        WebDriverWait(driver, 10).until((EC.staleness_of(loc)))




