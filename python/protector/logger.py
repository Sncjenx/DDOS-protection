from datetime import datetime

def log_event(category: str, message: str):
    """
    Logs an event with a timestamp and category.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{category}] {message}")
