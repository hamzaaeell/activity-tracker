import tkinter as tk
from tkinter import messagebox
import json
import os

def show_consent_dialog():
    root = tk.Tk()
    root.withdraw()
    
    consent = messagebox.askyesno(
        "Employee Monitoring Agreement",
        "This software will track your work activity, including:\n"
        "- Active/Inactive time\n"
        "- Occasional screenshots for productivity analysis\n\n"
        "Do you agree to proceed?"
    )
    
    if consent:
        config_path = os.path.join("app", "utils", "config.json")
        with open(config_path, "r+") as f:
            config = json.load(f)
            config["user_consent"] = True
            f.seek(0)
            json.dump(config, f)
    
    root.destroy()
    return consent
