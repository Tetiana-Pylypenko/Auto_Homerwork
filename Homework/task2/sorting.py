from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

website_url = "https://demowebshop.tricentis.com/gift-cards"
driver = webdriver.Chrome() 
driver.get(website_url)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

def test_sort_items_A_Z(): #Sorting by Name A to Z 
     
   sorting_dropdown = wait.until(EC.presence_of_element_located((By.ID, "products-orderby")))
   select = Select(sorting_dropdown)

   select.select_by_visible_text("Name: A to Z")
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=page-body]")))

   names = driver.find_elements(By.CSS_SELECTOR, ".product-title a")
   names_array = []
   for i in names:
        t = i.text
        names_array.append(t)
    
   assert names_array == sorted(names_array), "Test Failed: Products are not sorted correctly by 'Name from A to Z' option."   

def test_sort_items_Z_A(): #Sorting by Name Z to A
    wait = WebDriverWait(driver, 10)
    sorting_dropdown = wait.until(EC.presence_of_element_located((By.ID, "products-orderby")))
    select = Select(sorting_dropdown)

    select.select_by_visible_text("Name: Z to A")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=page-body]")))
    names = driver.find_elements(By.CSS_SELECTOR, ".product-title a")
    names_array = []

    for i in names:
        t = i.text
        names_array.append(t)
        
    assert names_array == sorted(names_array, reverse=True), "Test Failed: Products are not sorted correctly by 'Name from Z to A' option."  

def test_sort_items_high_low(): #Sorting by Price: Hight to Low
    wait = WebDriverWait(driver, 10)
    sorting_dropdown = wait.until(EC.presence_of_element_located((By.ID, "products-orderby")))
    select = Select(sorting_dropdown)

    select.select_by_visible_text("Price: High to Low")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=page-body]")))
    prices = driver.find_elements(By.CSS_SELECTOR, ".price.actual-price")
    prices_array = []

    for i in prices:
        t = float(i.text)
        prices_array.append(t) 
        
    assert prices_array == sorted(prices_array, reverse=True), "Test Failed: Products are not sorted correctly by 'Price: High to Low' option."  

def test_sort_items_low_high(): #Sorting by Price: Low to Hight
    wait = WebDriverWait(driver, 10) 
    sorting_dropdown = wait.until(EC.presence_of_element_located((By.ID, "products-orderby")))
    select = Select(sorting_dropdown)

    select.select_by_visible_text("Price: Low to High")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=page-body]")))
    prices = driver.find_elements(By.CSS_SELECTOR, ".price.actual-price")
    prices_array = []

    for i in prices:
        t = float(i.text)
        prices_array.append(t) 
        
    assert prices_array == sorted(prices_array), "Test Failed: Products are not sorted correctly by 'Price: Low to High' option." 


    driver.quit()
