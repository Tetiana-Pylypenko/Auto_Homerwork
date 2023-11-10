from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.parametrize("browser", ["chrome", "firefox"])

def test_subgroup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get("https://demowebshop.tricentis.com/")

    computers_menu = driver.find_element(By.LINK_TEXT, "Computers").click()

    # Locate the sub-groups under 'Computers'
    sub_groups = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//ul[@class='sublist']/li/a")))
   
    # Verify the names and count of sub-groups
    expected_sub_group_names = ["Desktops", "Notebooks", "Accessories"]

    assert len(sub_groups) == len(expected_sub_group_names), "Test Failed: Incorrect number of sub-groups under 'Computers'."

    sub_group_names = [sub_group.text for sub_group in sub_groups]
    
    assert all(name in sub_group_names for name in expected_sub_group_names), "Test Failed: Sub-group names do not match."

    driver.quit()
