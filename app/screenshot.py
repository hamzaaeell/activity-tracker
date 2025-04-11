import pyautogui
import time
import os
import json
from .utils.encryption import encrypt_data
from .aws_client import AWSClient

class ScreenshotMonitor:
    def __init__(self, encryption_key: str):  # Accept encryption key
        self.encryption_key = encryption_key
        self.aws = AWSClient()

    def capture_screenshot(self):
        # Capture screenshot
        screenshot = pyautogui.screenshot()
        temp_file = f"screenshot_{int(time.time())}.png"
        screenshot.save(temp_file)
        
        # Encrypt and upload
        with open(temp_file, "rb") as f:
            screenshot_data = f.read()  # Read raw bytes
            encrypted_data = encrypt_data(screenshot_data, self.encryption_key)  # Use screenshot bytes
        
        # Save encrypted data to a new file
        encrypted_file = f"encrypted_{temp_file}"
        with open(encrypted_file, "wb") as f:
            f.write(encrypted_data)
        
        # Upload encrypted file
        self.aws.upload_file(encrypted_file, f"screenshots/{encrypted_file}")
        
        # Cleanup
        os.remove(temp_file)
        os.remove(encrypted_file)