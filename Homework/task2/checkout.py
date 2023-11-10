from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_checkout_item():

    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument("--guest")
    driver = webdriver.Chrome(options=chrome_opt)

    driver.get("https://demowebshop.tricentis.com/apparel-shoes")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=product-grid]")))

    product = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Blue and green Sneaker")))
    product.click()

    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=add-to-cart-button-28]")))
    add_to_cart_button.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p[class=content]")))

    shopping_cart = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li[id=topcartlink]")))
    shopping_cart.click()

    # Wait for a moment to allow the item to be added to the cart (you may need to adjust the wait time)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*=shopping-cart-page]")))

    # Check agreement checkbox and press Checkout button
    agree_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
    agree_checkbox.click()
    checkout = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=checkout-buttons]")))
    checkout.click()

    # Press Checkout as Guest
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*=checkout-as-guest-or-register-block]")))
    checkout_as_guest = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[class*=checkout-as-guest-button]")))
    checkout_as_guest.click()

    # Wait Checkout page loaded and start checkout process
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*=checkout-page]")))

    # Billing Address section filling out
    driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("John")
    driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("Dooom")
    driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("john-moon@example.com")
    driver.find_element(By.ID, "BillingNewAddress_City").send_keys("London")
    driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Onewall 11/11")
    driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("123453")
    driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("1234567")

    country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId")))
    select = Select(country_dropdown)
    select.select_by_visible_text("Canada")

    driver.find_element(By.CSS_SELECTOR, "input[class*=new-address-next-step-button]").click()

    wait.until(EC.presence_of_element_located((By.ID, "checkout-step-shipping")))

    # Shipping Address section
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=PickUpInStore]"))).click()
    driver.find_elements(By.CLASS_NAME, "button-1.new-address-next-step-button")[1].click()

    # Shipping method section
    wait.until(EC.presence_of_element_located((By.ID, "checkout-step-shipping-method")))
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-1.payment-method-next-step-button"))).click()
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-1.payment-info-next-step-button"))).click()
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-1.confirm-order-next-step-button"))).click()

    # Check the confirmation page
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "page-title"), "Thank you"))
    confirm_message = driver.find_element(By.CLASS_NAME, "title").text

    assert confirm_message == 'Your order has been successfully processed!', "Test Failed: Checkout is not completed"

    driver.quit()