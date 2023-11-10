from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://EPAM.com')
driver.maximize_window()

def test_qwe():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    expected_policies_list1 = ["INVESTORS", "OPEN SOURCE", "PRIVACY POLICY"]
    expected_policies_list2 = ["COOKIE POLICY", "APPLICANT PRIVACY NOTICE", "WEB ACCESSIBILITY"]

    # Locate and verify the first policies list
    policies_list1 = driver.find_element(By.CSS_SELECTOR, ".policies-left")
    policies_text1 = policies_list1.text

    for policy in expected_policies_list1:
        assert policy in policies_text1, f"Test Failed: {policy} is missing from the first policies list." 

        # if policy not in policies_text1:
        #     print(f"Test Failed: {policy} is missing from the first policies list.")
        #     break

    # Locate and verify the second policies list
    policies_list2 = driver.find_element(By.CSS_SELECTOR, ".policies-right")
    policies_text2 = policies_list2.text

    for policy in expected_policies_list2:
        assert policy in policies_text2, f"Test Failed: {policy} is missing from the second policies list." 
 # if policy not in policies_text2:
        #     print(f"Test Failed: {policy} is missing from the second policies list.")
        #     break
  

       
#     else:
#         print("Test Passed: All expected policies are found in both lists.")

# finally:
    driver.quit()