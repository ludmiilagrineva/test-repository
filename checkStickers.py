import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver



@pytest.fixture
def driver (request):
    wd = webdriver.Chrome()

    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/en/")
    time.sleep(1)
    elements = driver.find_elements(By.CSS_SELECTOR, "li.product")
    count=len(elements)

    for i in range(count):
        elements[i].find_element(By.CSS_SELECTOR, ".sticker")




