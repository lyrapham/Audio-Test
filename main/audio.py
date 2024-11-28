
import os
import time
import subprocess
import pygetwindow as gw
from mutagen.mp3 import MP3

# Media Player will be closed after the audio ended = duration 
def get_audio_duration(audio_file_path):
    try:
        audio = MP3(audio_file_path)
        return round(audio.info.length,2)
    except Exception as e:
        raise Exception(f"Error in (4) Play Audio - Get Audio Duration step: {str(e)}")
    

def play_audio(audio_file_path):
    print("\nProcessing (4) Play Audio step...")
    try:
        audio_file_path = os.path.abspath(audio_file_path)
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"Audio file '{audio_file_path}' does not exist.")

        # Get and validate audio duration
        audio_duration = get_audio_duration(audio_file_path)
        if not audio_duration:
            raise ValueError("Unable to determine audio duration.")
        print(f"Audio duration: {audio_duration} seconds")

        # Play audio
        subprocess.Popen(f'start "" "{audio_file_path}"', shell=True)
        print(f"Playing audio file '{audio_file_path}'...")

        time.sleep(3)  # Allow media player to launch

        # Find the media player window
        media_player_window = next(
            (w for w in gw.getAllTitles() if "media player" in w.lower()), None
        )
        if not media_player_window:
            raise RuntimeError("Media player window not found after launching the audio.")

        print("Media player window detected.")

        # Monitor playback
        start_time = time.time()
        while time.time() - start_time < audio_duration:
            # Check if the media player window still exists
            current_windows = gw.getAllTitles()
            if media_player_window not in current_windows:
                raise RuntimeError("Media player window closed unexpectedly before playback completed.")

            #print(f"Playing... {int(time.time() - start_time)}s elapsed.")
            time.sleep(1)

        print("Playback duration completed.")

        # Close the media player window if still open
        for window in gw.getWindowsWithTitle(media_player_window):
            window.close()
            print("Media player window closed after playback.")
    except Exception as e:
        raise Exception(f"Error in (4) Play Audio step: {e}")