# JarvisMD Automation Test - Audio

- [Overview](#overview)
- [Features Tested](#features-tested)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Repository Structure](#repository-structure)
- [Contributing](#contributing)

## Overview

This repository contains Selenium-based automation scripts for testing the audio functionalities of the JarvisMD platform by HealthBridge AI. The tests ensure the reliability and efficiency of audio processing workflows in both:
- MVP Environment
- Test Environment

## Features Tested

The following features are validated as part of the audio test suite:

1. Login Functionality: Ensures successful login with valid credentials and handles invalid login scenarios.
- For MVP Environment, after log in, there is 10 seconds waittime for user to manually write in the One-time code.
2. Patient Information Filling Workflow: Selects and verifies the correct patient profile for audio testing.
3. Session Management: Validates the start and completion of an audio session.
- Skip "Introduction" Pop Up with "Don't Show Again" button. Automatically detect if this pop up exists, if not, skipped.
- Start New Session.
4. Audio Playback: Tests playback of audio files to ensure accurate audio rendering within the platform.
- Play Audio (.mp3, .wav) by default media player (For Windows, it's Window Media Player).
- Get Audio Duration.
5. Audio Recording: Ensures that the platform successfully records and stores audio files for the session.
- Start Recording.
- Write [Audio Name] - [Time Now] format in ScratchPad to easy track later
- Stop Recording after Audio Duration ended.
6. Screenshot Capture: Captures a screenshot for reporting and validation.
- Currently unable to capture fullpage screenshot, will update later. - Nov 26, 2024
- Only take screenshot when the final result is ready.
7. Survey Management: Skips survey prompts post-session, ensuring smooth workflow continuity

## Setup Instructions

### Prerequisites
- **Python**: Version 3.7 or higher (3.12.1 as used).
- **Google Chrome**: Latest version installed.

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/HealthBridge-AI/jarvismd-automation-tests.git
   cd audio-test

2. Install Dependencies: Use pip to install the necessary package:
   ```bash
   pip install -r requirements.txt
3. Configure Environment Variables: For secure storage of login credentials in main.py:

   Config all the variables with #change here in main.py 

    - Folder Paths:
   ```bash
   audio_folder_path = r"AUDIO-FOLDER-LINK"
   test_screenshot_path = r"TEST-ENV-SCREENSHOT-FOLDER-LINK"
   mvp_screenshot_path = r"MVP-ENV-SCREENSHOT-FOLDER-LINK"
   ```

   - Account for MVP & Test Environment:
   ``` bash
   username = "USER-NAME"
   password = ""
   url = "https://mvp.healthbridgeai.com/"
   wait_time = 10 # For manually put in One-time code in MVP Environment testing
   patient_id = "PATIENT-ID"
   ```

## Usage

   To execute Audio Test, run:
   ```bash
   python main.py
   ```

## Repository Structure
- requirements.txt: Lists required Python packages for running the automation tests.
- README.md: Documentation for the repository.

   


