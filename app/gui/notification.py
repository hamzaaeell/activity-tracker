import tkinter as tk
from tkinter import messagebox
from ..utils.logger import Logger

class Notification:
    def __init__(self):
        self.logger = Logger()
        
    def show_screenshot_alert(self):
        """Display a temporary notification when a screenshot is taken"""
        root = tk.Tk()
        root.withdraw()
        root.after(3000, root.destroy)  # Auto-close after 3 seconds
        
        messagebox.showinfo(
            "Activity Monitor",
            "A productivity screenshot was captured at " + time.strftime("%H:%M:%S")
        )
        
        self.logger.log_notification("Screenshot captured at " + time.strftime("%H:%M:%S"))
        root.destroy()
