import json
import time
from pathlib import Path
from .utils.encryption import encrypt_data

class Tracker:
    def __init__(self, encryption_key: str):
        self.start_time = None
        self.encryption_key = encryption_key
        self.data_dir = Path("data/logs")
        self.data_dir.mkdir(parents=True, exist_ok=True) 

    def start_session(self):
        self.start_time = time.time()
        self._log_activity("SESSION_START")

    def end_session(self):
        if self.start_time:
            duration = time.time() - self.start_time
            self._log_activity("SESSION_END", duration=duration)

    def _log_activity(self, event_type: str, duration: float = 0):
        log = {
            "timestamp": time.time(),
            "event": event_type,
            "duration": duration
        }
        encrypted_log = encrypt_data(
            json.dumps(log).encode(),
            self.encryption_key
        )
        log_file = self.data_dir / f"log_{int(time.time())}.bin"
        log_file.write_bytes(encrypted_log)