from selenium import webdriver
from audio_test import audio_test

# Audio and screenshot paths
audio_folder_path = r"AUDIO-FOLDER" # Change Here
test_screenshot_path = r"TEST-ENV-SCREENSHOT-FOLDER" # Change Here
mvp_screenshot_path = r"MVP-ENV-SCREENSHOT-FOLDER" # Change Here

def main():
    try:
        # Prompt for environment selection
        choice = input("Select Environment for Testing2:\n1. MVP Environment\n2. Testing Environment\nEnter 1 or 2: ").strip()

        if choice not in ["1", "2"]:
            print("Invalid choice. Please enter 1 or 2.")
            return  # Exit the program if the choice is invalid

        # Define variables based on choice
        if choice == "1":
            print("Running tests on MVP Environment...")
            username = "USER-NAME" # Change Here
            password = "PASSWORD" # Change Here
            url = "https://mvp.healthbridgeai.com/" # Change Here
            wait_time = 10
            patient_id = "PATIENT" # Change Here
            screenshot_path = mvp_screenshot_path

        elif choice == "2":
            print("Running tests on Testing Environment...")
            username = "USER-NAME" # Change Here
            password = "PASSWORD" # Change Here
            url = "https://mvp.healthbridgeai.com:5000/" # Change Here
            wait_time = 0
            patient_id = "PATIENT" # Change Here
            screenshot_path = test_screenshot_path

        # Initialize the browser only after choice
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        
        # Call the audio_test function
        driver = webdriver.Chrome(options=chrome_options)
        audio_test(driver, username, password, audio_folder_path, screenshot_path, url, wait_time, patient_id)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Closing the driver.")
        driver.quit()  # Close browser

if __name__ == "__main__":
    main()
