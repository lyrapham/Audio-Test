import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import pytz # type: ignore

def write_to_scratchpad(driver, audio_name):
    est = pytz.timezone("America/New_York")
    current_time = datetime.now(est).strftime("%Y-%m-%d %H:%M:%S")
    scratch_note = f"{audio_name} - {current_time}"

    # Wait for the textarea element to be present and visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "note"))
    )

    # Find the textarea and input the text
    textarea = driver.find_element(By.ID, "note")
    textarea.clear()  # Clear any existing text (optional)
    textarea.send_keys(scratch_note)
    print(f"Successfully wrote to the textarea: {scratch_note}")


def skip_survey(driver):
    print(f"\nProcessing (8) Skip Survey step...")
    try:
        # Step 1: Click the dropdown menu
        dropdown_menus = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.ant-select-selection-search-input"))
        )

        for dropdown_menu in dropdown_menus:
            try:
                if "rc_select" in dropdown_menu.get_attribute("id"):  # Check if the ID contains "rc_select"
                    dropdown_menu.click()
                    print(f"Dropdown menu with ID '{dropdown_menu.get_attribute('id')}' clicked successfully.")
                    break
            except Exception as e:
                raise Exception(f"Failed to click dropdown menu with ID '{dropdown_menu.get_attribute('id')}': {e}")

        # Step 2: Select the "1 - 5 minutes" option

        try:
            option = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-select-dropdown')]//div[@title='1 - 5 minutes']"))
            )
            option.click()
            print("Option '1 - 5 minutes' selected successfully.")
        except Exception as e:
            raise Exception(f"Failed to choose Option '1-5 minutes': {e}")


        # Step 3: Click the "Submit" button
        submit_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ant-btn') and span[text()='Submit']]"))
        )
        submit_button.click()
        print("Submit button clicked successfully.")

    except TimeoutException as e:
        raise TimeoutException(f"Error in (8) Skip Survey step: {str(e)}")


def keep_website_active(driver, seconds):
    print(f"\nProcessing (7) Keep Website Active step...")
    print(f"Keeping the website active for {seconds} seconds...")
    time.sleep(seconds)
    
    try:
        # Correct XPath for the "New Session" button (first button)
        xpath = "//li[@class='ant-menu-overflow-item ant-menu-item ant-menu-item-only-child ant-pro-base-menu-horizontal-menu-item' and .//span[text()='New Session']]"
        
        # Wait for the button to be clickable
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        
        # Locate the button
        new_session_button = driver.find_element(By.XPATH, xpath)
        
        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView();", new_session_button)

        # Attempt to click using ActionChains
        try:
            actions = ActionChains(driver)
            actions.move_to_element(new_session_button).click().perform()
            print("ActionChains: New Session button clicked")
        except Exception as e:
            print(f"ActionChains click failed: {e}")

        # Fallback to JavaScript click
        try:
            driver.execute_script("arguments[0].click();", new_session_button)
            print("JavaScript: New Session button clicked")
        except Exception as e:
            print(f"JavaScript click failed: {e}")

    except Exception as e:
        raise Exception(f"Error in (7) Keep Website Active step: {str(e)}")



def click_start_first_session(driver):
    print(f"\nProcessing (2) Click Start First Session step...")
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".ant-btn-primary.ant-btn-color-primary"))
        )
        start_session_button = driver.find_element(By.CSS_SELECTOR, ".ant-btn-primary.ant-btn-color-primary")
        start_session_button.click()
        print("Start Session button clicked")
    except Exception as e:
        raise Exception(f"Error in (2) Click Start First Session step {str(e)}")
    

def dont_show_again_button(driver):
    print("\nProcessing (0) Don't show again step...")

    try:
        # Wait for the button to appear (up to 15 seconds)
        dont_show_again_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='not-show-again-button']"))
        )
        print("Button is clickable. Attempting to click...")

        # Click the button using JavaScript to avoid potential overlay issues
        driver.execute_script("arguments[0].click();", dont_show_again_button)
        print("'Don't show this again' button clicked successfully.")
    
    except TimeoutException:
        # Skip the function if the button doesn't appear
        print("Timeout: 'Don't show this again' button not found. Skipping this step.")
        return  # Exit the function without raising an exception
    
    except StaleElementReferenceException:
        print("Stale element detected. Re-fetching the button...")
        try:
            dont_show_again_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='not-show-again-button']"))
            )
            driver.execute_script("arguments[0].click();", dont_show_again_button)
            print("'Don't show this again' button clicked successfully after re-fetching.")
        except Exception as e:
            print(f"Failed to re-fetch and click the button: {str(e)}")
    
    except Exception as e:
        print(f"Error in (0) Don't show again step: {str(e)}")


def start_recording(driver, audio_name):
    print(f"\nProcessing (3) Start Recording step...")
    try:
        record_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ant-btn-circle.ant-btn-primary.ant-btn-icon-only"))
        )
        
        # Click the recording button with JavaScript
        driver.execute_script("arguments[0].click();", record_button)
        print("Recording button clicked. Starting audio...")

        consent_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'ant-btn-primary') and contains(., 'Confirm Consent Obtained')]"))
        )

        # Click the consent button with JavaScript
        driver.execute_script("arguments[0].click();", consent_button)
        print("Consent confirmed using JavaScript click.")

        try:
            write_to_scratchpad(driver, audio_name)
        except Exception as e:
            raise Exception(f"Error in (3) Start Recording - Write to Scratchpad step: {str(e)}")

    except Exception as e:
            raise Exception(f"Error in (3) Start Recording - step: {str(e)}")


def stop_recording(driver):
    print("\nProcessing (5) Stop Recording step...")
    try:
        stop_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".ant-btn-round.ant-btn-primary.ant-btn-color-primary.ant-btn-variant-solid.ant-btn-lg"))
        )
        stop_button.click()
        print("Stop Recording button clicked successfully.")

        while True: #Only move to next step if the Referral Button found
            try:
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='referral-letter-btn']"))
                )
                print("Element is found!")
                break  
            except TimeoutException:
                print("Still waiting for the element... Retrying.")
                time.sleep(5) 

        print("Button with data-testid='referral-letter-btn' found on the page.")
        print("Waiting for 5 seconds...")
        time.sleep(2)
    except Exception as e:
        raise Exception(f"Error in (5) Stop Recording step: {e}")