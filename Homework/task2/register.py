from selenium import webdriver
from selenium.webdriver.common.by import By


def test_user_registration():
    driver = webdriver.Chrome() 
    driver.get("https://demowebshop.tricentis.com/")

    register_link = driver.find_element(By.LINK_TEXT, "Register")
    register_link.click()

    driver.find_element(By.ID, "gender-male").click()
    driver.find_element(By.ID, "FirstName").send_keys("John")
    driver.find_element(By.ID, "LastName").send_keys("Dooom")
    driver.find_element(By.ID, "Email").send_keys("john-nnoon@example.com")
    driver.find_element(By.ID, "Password").send_keys("password123")
    driver.find_element(By.ID, "ConfirmPassword").send_keys("password123")

    driver.find_element(By.ID, "register-button").click()

    driver.implicitly_wait(5)
    
    registration_success_message = driver.find_element(By.CSS_SELECTOR, ".result").text
    assert "Your registration completed" in registration_success_message, "Test Failed: User registration was not successful."

    driver.quit()
