from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.parametrize("browser", ["chrome", "firefox"])

def test_wishlist(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get("https://demowebshop.tricentis.com/jewelry")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    product = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Black & White Diamond Heart")))
    product_text = product.text
    product.click()

    add_to_wish_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=add-to-wishlist-button-14]")))
    add_to_wish_button.click()

    #Wait for a banner 'The product has been added to your wishlist'
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p[class=content]")))

    wish_list = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class=ico-wishlist]")))
    wish_list.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*=wishlist-page]")))

    wish_product = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Black & White Diamond Heart")))
    wish_product_text = wish_product.text

    assert wish_product_text == product_text, "Test Failed: Item has not been added to the wishlist."

    driver.quit()
