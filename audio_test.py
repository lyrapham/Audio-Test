import os
from selenium import webdriver
import mimetypes
from main.screenshot import take_fullpage_screenshot
from main.login import open_website, enter_credentials, login_button
from main.select_patient_information import select_patient_information
from main.audio import play_audio
from main.wait import wait_countdown
from main.website_interactions import (
    click_start_first_session, 
    keep_website_active, 
    dont_show_again_button, 
    start_recording, 
    stop_recording,
    skip_survey
)

# Start
def safe_execute(step_name, step_function, *args, **kwargs):
    try:
        step_function(*args, **kwargs)  # Call the step function
    except Exception as e:
        print(f"[Safe Excute] - {step_name} {e}")
        return False  # Return False on error
    return True  

def processing_audio_test(driver, audio_file_path, screenshot_path, audio_name, patient_id):
    steps = [
        ("(1) Select Patient Information", select_patient_information, driver, patient_id),
        ("(2) Click Start First Session", click_start_first_session, driver),
        ("(3) Start Recording step", start_recording, driver, audio_name),
        ("(4) Play Audio", play_audio, audio_file_path),
        ("(5) Stop Recording", stop_recording, driver),
        ("(0) Don\'t show again button", dont_show_again_button, driver),
        ("(6) Take Fullpage Screenshot", take_fullpage_screenshot, driver, screenshot_path, audio_name),
        ("(7) Keep Website Active", keep_website_active, driver, 5),
        ("(8) Skip Survey After Recording", skip_survey, driver)
    ]

    for step_name, func, *args in steps:
        # Call safe_execute and break the loop if it fails
        if not safe_execute(step_name, func, *args):
            print(f"Execution stopped at step: {step_name}")
            break


def audio_test(driver, username, password, audio_folder_path, screenshot_path, url, seconds, patient_id):
    try:
        # Step (0) - Open Website / Enter Credentials / Log In / Don't show again
        open_website(driver, url)
        enter_credentials(driver, username, password)
        login_button(driver)
        wait_countdown(seconds)
        dont_show_again_button(driver)

        list_audio = []
        for file in os.listdir(audio_folder_path):
            filepath = os.path.join(audio_folder_path, file)
            mime_type, _ = mimetypes.guess_type(filepath)
            if mime_type and mime_type.startswith('audio'):
                list_audio.append(file)
        print(f"There are {len(list_audio)} audio files in folder. \n Audio files to process: {'\n'.join(list_audio)}")

        for file in list_audio:
            audio_file_path = os.path.join(audio_folder_path, file)
            print(f"Processing audio file: {audio_file_path}")
            processing_audio_test(driver, audio_file_path, screenshot_path, file, patient_id)

    except Exception as e:
        raise Exception(f"Audio Test failed: {e}")

    finally:
        print("Closing the driver.")
        driver.quit()
