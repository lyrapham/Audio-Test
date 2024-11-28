from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

def take_fullpage_screenshot(driver, screenshot_path, audio_name):
    print(f"\nProcessing (6) Take Fullpage Screenshot step...")
    try:
        # Wait for the button to be present on the page --> able to take a picture
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='referral-letter-btn']"))
        )
        print("Button with data-testid='referral-letter-btn' found on the page.")

        web_page_height = driver.execute_script("""
            return Math.max(
                document.body.scrollHeight,
                document.body.offsetHeight,
                document.documentElement.clientHeight,
                document.documentElement.scrollHeight,
                document.documentElement.offsetHeight
            );
        """)

        driver.set_window_size(1920, web_page_height)  # Fixed width, dynamic height
        print(f"Window set to width: 1920, height: {web_page_height}")

        name = f"{screenshot_path}\\{audio_name[:-4]}.png"

        # Check if the file exists and delete it
        if os.path.exists(name):
            os.remove(name)
            print(f"Existing screenshot '{name}' deleted.")

        # Capture the screenshot
        driver.save_screenshot(name)
        print(f"Screenshot saved to {name}")

    except Exception as e:
        raise Exception(f"Error in (6) Take Fullpage Screenshot step: {str(e)}")
