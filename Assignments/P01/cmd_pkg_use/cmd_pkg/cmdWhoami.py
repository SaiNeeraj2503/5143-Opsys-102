import os

def whoami(**kwargs):
    username = os.getlogin()
    return f"Current user: {username}"
