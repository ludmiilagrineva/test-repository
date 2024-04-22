import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def isGreyRegularPrice(color):
    r, g, b, a = color[5:-1].split(",")
    r=int(r)
    g=int(g)
    b=int(b)
    if r==g==b:
        return True
    else:
        return False

def isRedSalePrice(color):
    r, g, b, a = color[5:-1].split(",")
    r = int(r)
    g = int(g)
    b = int(b)
    if g==b==0 and r!=0:
        return True
    else:
        return False

def isSalePriceSizeBiggerRegular(sizeSalePrice, sizeRegularPrice):
    sizeSalePrice=float(sizeSalePrice[:len(sizeSalePrice)-2])
    sizeRegularPrice=float(sizeRegularPrice[:len(sizeRegularPrice)-2])

    if sizeSalePrice>sizeRegularPrice:
        return True
    else:
        return False

@pytest.fixture
def driver (request):
    wd=webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/en/")

    # Main page
    productNameMainPage = driver.find_element(By.XPATH,"//div[@id=\"box-campaigns\"]/div/ul/li[1]/a/div[@class=\"name\"]").text
    regularPriceMainPage = driver.find_element(By.XPATH,"//div[@id=\"box-campaigns\"]/div/ul/li[1]/a/div[@class=\"price-wrapper\"]/s[@class=\"regular-price\"]").text
    salePriceMainPage = driver.find_element(By.XPATH,"//div[@id=\"box-campaigns\"]/div/ul/li[1]/a/div[@class=\"price-wrapper\"]/strong[@class=\"campaign-price\"]").text
    tagRegularPriceMainPage = driver.find_element(By.XPATH,"//div[@id=\"box-campaigns\"]/div/ul/li[1]/a/div[@class=\"price-wrapper\"]/s[@class=\"regular-price\"]").tag_name
    colorRegularPriceMainPage = driver.find_element(By.XPATH,"//div[@id=\"box-campaigns\"]/div/ul/li[1]/a/div[@class=\"price-wrapper\"]/s[@class=\"regular-price\"]").value_of_css_property("color")
    tagSalePriceMainPage = driver.find_element(By.XPATH,"//div[@id=\"box-campaigns\"]/div/ul/li[1]/a/div[@class=\"price-wrapper\"]/strong[@class=\"campaign-price\"]").tag_name
    colorSalePriceMainPage = driver.find_element(By.XPATH,"//div[@id=\"box-campaigns\"]/div/ul/li[1]/a/div[@class=\"price-wrapper\"]/strong[@class=\"campaign-price\"]").value_of_css_property("color")
    sizeRegularPriceMainPage = driver.find_element(By.XPATH,"//div[@id=\"box-campaigns\"]/div/ul/li[1]/a/div[@class=\"price-wrapper\"]/s[@class=\"regular-price\"]").value_of_css_property("font-size")
    sizeSalePriceMainPage = driver.find_element(By.XPATH,"//div[@id=\"box-campaigns\"]/div/ul/li[1]/a/div[@class=\"price-wrapper\"]/strong[@class=\"campaign-price\"]").value_of_css_property("font-size")

    # Product page
    driver.find_element(By.XPATH, "//div[@id=\"box-campaigns\"]/div/ul/li[1]/a").click()

    productNameProductPage = driver.find_element(By.XPATH, "//div[@id=\"box-product\"]/div/h1[@class=\"title\"]").text
    regularPriceProductPage = driver.find_element(By.XPATH,"//div[@class=\"content\"]/div[@class=\"information\"]/div/s[@class=\"regular-price\"]").text
    salePriceProductPage = driver.find_element(By.XPATH,"//div[@class=\"content\"]/div[@class=\"information\"]/div/strong[@class=\"campaign-price\"]").text
    tagRegularPriceProductPage = driver.find_element(By.XPATH,"//div[@class=\"content\"]/div[@class=\"information\"]/div/s[@class=\"regular-price\"]").tag_name
    colorRegularPriceProductPage = driver.find_element(By.XPATH,"//div[@class=\"content\"]/div[@class=\"information\"]/div/s[@class=\"regular-price\"]").value_of_css_property("color")
    tagSalePriceProductPage = driver.find_element(By.XPATH,"//div[@class=\"content\"]/div[@class=\"information\"]/div/strong[@class=\"campaign-price\"]").tag_name
    colorSalePriceProductPage = driver.find_element(By.XPATH,"//div[@class=\"content\"]/div[@class=\"information\"]/div/strong[@class=\"campaign-price\"]").value_of_css_property("color")
    sizeRegularPriceProductPage = driver.find_element(By.XPATH,"//div[@class=\"content\"]/div[@class=\"information\"]/div/s[@class=\"regular-price\"]").value_of_css_property("font-size")
    sizeSalePriceProductPage = driver.find_element(By.XPATH,"//div[@class=\"content\"]/div[@class=\"information\"]/div/strong[@class=\"campaign-price\"]").value_of_css_property("font-size")

    if (productNameMainPage != productNameProductPage or regularPriceMainPage != regularPriceProductPage or
            salePriceMainPage != salePriceProductPage or tagRegularPriceMainPage != "s" or tagRegularPriceProductPage != "s" or
            not isGreyRegularPrice(colorRegularPriceMainPage) or not isGreyRegularPrice(colorRegularPriceProductPage) or
            tagSalePriceMainPage != "strong" or tagSalePriceProductPage != "strong" or not isRedSalePrice(colorSalePriceMainPage) or
            not isRedSalePrice(colorSalePriceProductPage) or not isSalePriceSizeBiggerRegular(sizeSalePriceMainPage,sizeRegularPriceMainPage) or
            not isSalePriceSizeBiggerRegular(sizeSalePriceProductPage, sizeRegularPriceProductPage)):
        pytest.fail("Товары не равны")
