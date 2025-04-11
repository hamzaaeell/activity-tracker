import pyautogui
import time
import os
import json
from .utils.encryption import encrypt_data
from .aws_client import AWSClient

class ScreenshotMonitor:
    def __init__(self, encryption_key: str):  
        self.encryption_key = encryption_key
        self.aws = AWSClient()

    def capture_screenshot(self):
        screenshot = pyautogui.screenshot()
        temp_file = f"screenshot_{int(time.time())}.png"
        screenshot.save(temp_file)
        

        with open(temp_file, "rb") as f:
            screenshot_data = f.read()  
            encrypted_data = encrypt_data(screenshot_data, self.encryption_key) 
        
        encrypted_file = f"encrypted_{temp_file}"
        with open(encrypted_file, "wb") as f:
            f.write(encrypted_data)
        
        self.aws.upload_file(encrypted_file, f"screenshots/{encrypted_file}")
        
        os.remove(temp_file)
        os.remove(encrypted_file)