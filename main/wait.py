import time

def wait_countdown(seconds):

    print(f"Waiting for {seconds} seconds...")
    for remaining in range(seconds, 0, -1):
        print(f"Time remaining: {remaining} seconds", end="\r", flush=True)
        time.sleep(1)
    print(f"{seconds} seconds have passed.")
