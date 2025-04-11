import schedule
import time
import random
import json
import sys
from app.gui.consent import show_consent_dialog
from app.tracker import Tracker
from app.screenshot import ScreenshotMonitor
from app.utils.config_loader import load_config

def main():
    try:
        # Load configuration
        config = load_config()
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Configuration error: {str(e)}")
        sys.exit(1)

    # Check user consent
    if not show_consent_dialog():
        print("Consent denied. Exiting.")
        return

    # Initialize components with encryption key
    tracker = Tracker(config["encryption_key"])
    screenshot_monitor = ScreenshotMonitor(config["encryption_key"])

    # Start tracking session
    tracker.start_session()

    # Configure screenshot scheduling
    def screenshot_task():
        if random.random() < 0.5:  # 50% chance
            print("[Debug] Attempting screenshot capture...")
            screenshot_monitor.capture_screenshot()
            print("[TEST] Screenshot captured!")


    # schedule.every(30).to(60).minutes.do(screenshot_task)
    schedule.every(1).minutes.do(screenshot_task)

    # Main monitoring loop
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        tracker.end_session()
        print("\nMonitoring stopped gracefully.")

if __name__ == "__main__":
    main()