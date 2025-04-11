import json
from pathlib import Path

def load_config():
    config_path = Path(__file__).parent.parent / "utils" / "config.json"
    if not config_path.exists():
        raise FileNotFoundError(f"Missing config file: {config_path}")
    
    with open(config_path, "r") as f:
        return json.load(f)