import time
import json
from pathlib import Path
from .encryption import encrypt_data
from ..aws_client import AWSClient

class Logger:
    def __init__(self):
        self.aws = AWSClient()
        self.local_log_dir = Path("local_logs")
        self.local_log_dir.mkdir(exist_ok=True)

    def log_event(self, event_type: str, metadata: dict = None):
        """Log events like screenshots, app usage, etc."""
        log_entry = {
            "timestamp": time.time(),
            "event": event_type,
            "metadata": metadata or {}
        }
        
        encrypted_data = encrypt_data(
            json.dumps(log_entry).encode(), 
            "your-encryption-key-here"
        )
        local_file = self.local_log_dir / f"log_{time.time()}.bin"
        local_file.write_bytes(encrypted_data)
        
        self.aws.upload_file(
            str(local_file), 
            f"logs/{local_file.name}"
        )

    def log_notification(self, message: str):
        """Log when employees are notified about screenshots"""
        self.log_event("NOTIFICATION", {"message": message})
