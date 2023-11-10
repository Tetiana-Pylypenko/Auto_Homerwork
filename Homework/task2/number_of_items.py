from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest

@pytest.mark.parametrize("browser", ["chrome", "firefox"])

def test_number_of_items(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
 
    driver.get("https://demowebshop.tricentis.com/apparel-shoes")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    item_dropdown = wait.until(EC.presence_of_element_located((By.ID, "products-pagesize")))                                             
    select = Select(item_dropdown)

    # Get all the available options for the number of items
    show_options = select.options
    list_options = []
    
    for option in show_options:
        list_options.append(option.text)

    # Iterate through the options and select each one
    for option in list_options:
        item_dropdown = wait.until(EC.presence_of_element_located((By.ID, "products-pagesize")))
        select = Select(item_dropdown)
        select.select_by_visible_text(option)
        
        driver.implicitly_wait(5)

        # Verify that the number of items displayed matches the selected option
        displayed_items = driver.find_elements(By.CLASS_NAME, "item-box")
     
    assert len(displayed_items) == int(option), (f"Test Failed: Number of items displayed is not {option}.")

    driver.quit()