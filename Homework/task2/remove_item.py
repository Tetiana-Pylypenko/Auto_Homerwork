from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.parametrize("browser", ["chrome", "firefox"])

def test_remove_item(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    driver.get("https://demowebshop.tricentis.com/apparel-shoes")
    driver.maximize_window() 
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=product-grid]")))

    product = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Blue and green Sneaker")))
    product_name = product.text
    product.click()

    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=add-to-cart-button-28]")))
    add_to_cart_button.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p[class=content]")))

    shopping_cart = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li[id=topcartlink]")))
    shopping_cart.click()

    # Wait for a moment to allow the item to be added to the cart (you may need to adjust the wait time)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*=shopping-cart-page]")))

    # Verify that the item is in the cart
    cart_product = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Blue and green Sneaker")))
    cart_product_name = cart_product.text
    assert cart_product_name == product_name, "Test Failed: Item has not been added to the card."

    remove_checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name=removefromcart]")))
    remove_checkbox.click()

    update_cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name=updatecart]")))
    update_cart.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*=shopping-cart-page]")))

    removed_cart_product = len(driver.find_elements(By.LINK_TEXT, "Blue and green Sneaker"))

    assert removed_cart_product == 0, 'The item is not removed'

    driver.quit()
