from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.parametrize("browser", ["chrome", "firefox"])

def test_title(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get('https://EPAM.com')
    driver.maximize_window()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    expected_policies_list1 = ["INVESTORS", "OPEN SOURCE", "PRIVACY POLICY"]
    expected_policies_list2 = ["COOKIE POLICY", "APPLICANT PRIVACY NOTICE", "WEB ACCESSIBILITY"]

    # Locate and verify the first policies list
    policies_list1 = driver.find_element(By.CSS_SELECTOR, ".policies-left")
    policies_text1 = policies_list1.text

    for policy in expected_policies_list1:
        assert policy in policies_text1, f"Test Failed: {policy} is missing from the first policies list." 

    # Locate and verify the second policies list
    policies_list2 = driver.find_element(By.CSS_SELECTOR, ".policies-right")
    policies_text2 = policies_list2.text

    for policy in expected_policies_list2:
        assert policy in policies_text2, f"Test Failed: {policy} is missing from the second policies list." 

    driver.quit()