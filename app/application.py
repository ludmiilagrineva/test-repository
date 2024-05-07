from selenium import webdriver
from pages.cartPage import CartPage
from pages.mainPage import MainPage
from pages.productPage import ProductPage

class Application:

    def __init__(self, driver):
        self.mainPage = MainPage(driver)
        self.productPage=ProductPage(driver)
        self.cartPage = CartPage(driver)

    def addProductsToCart(self, driver):
        self.mainPage.moveToTheMainPage()
        for i in range(1, 4):
            self.mainPage.moveToTheProductToCart(driver, i)
            if self.productPage.isFindedElementSize(driver):
                self.productPage.selectSizeDucks(driver)
            self.productPage.addProduct(driver)
            self.productPage.waitAddedToTheCart(driver, i)

    def removeProduct(self, driver):
        self.cartPage.moveToTheCartPage(driver)
        while not self.cartPage.isCartEmpty(driver):
            self.cartPage.removeProduct(driver)


