from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.parametrize("browser", ["chrome", "firefox"])

def test_login(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get("https://demowebshop.tricentis.com/")

    login_link = driver.find_element(By.LINK_TEXT, "Log in")
    login_link.click()

    driver.find_element(By.ID, "Email").send_keys("john-soon@example.com")
    driver.find_element(By.ID, "Password").send_keys("password123")

    driver.find_element(By.CSS_SELECTOR, "input[value='Log in']").click()

    driver.implicitly_wait(5)

    user_greeting = driver.find_element(By.CLASS_NAME, "account").text

    assert "john-soon@example.com" in user_greeting, "Test Failed: User login was not successful."

    driver.quit()