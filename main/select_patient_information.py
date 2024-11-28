from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def select_patient_information(driver, patient_id):
    print(f"\nProcessing (1) Select Patient Information step...")

    try:
        # Locate any dropdown with an ID containing "rc_select"
        dropdowns = driver.find_elements(By.CSS_SELECTOR, "[id^='rc_select']")
        
        if not dropdowns:
            raise Exception("No dropdown menus with 'rc_select' found.")
        
        for dropdown in dropdowns:
            try:
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable(dropdown)).click()
                print(f"Dropdown with ID '{dropdown.get_attribute('id')}' clicked successfully.")
                break 
            except TimeoutException:
                print(f"Dropdown with ID '{dropdown.get_attribute('id')}' not clickable. Trying the next option.")
        
        xpath = f"//div[contains(@class, 'ant-select-item-option-content') and text()='{patient_id}']"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath))).click()
        print(f"Patient ID '{patient_id}' selected.")

    except Exception as e:
        raise Exception(f"Error in (1) Select Patient Information step: {str(e)}")
