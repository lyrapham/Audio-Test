from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def open_website(driver, url):
    print(f"\nProcessing (0) Open Website step...")
    try:
        driver.maximize_window() 
        driver.get(url)
    except Exception as e:
        raise Exception(f"Error in (0) Open Website step: {str(e)}")



def enter_credentials(driver, username, password):
    print(f"\nProcessing (0) Enter Credentials step...")
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        

        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(username)
        print(f"Username {username} entered !")

        # Enter the password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        print(f"Password {password} entered!")

    except Exception as e:
        raise Exception(f"Error in (0) Enter Credentials step: {str(e)}")

def login_button(driver):
    print(f"\nProcessing (0) Log In step...")
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "kc-login"))
        )

        login_button = driver.find_element(By.ID, "kc-login")
        login_button.click()

    except Exception as e:
        raise Exception(f"Error in (0) Log In step: {str(e)}")
