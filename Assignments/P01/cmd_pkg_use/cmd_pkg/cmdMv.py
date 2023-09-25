import os
import shutil

def mv(**kwargs):
    if "params" in kwargs:
        params = kwargs["params"]
        if len(params) == 2:
            source = params[0]
            destination = params[1]
            try:
                shutil.move(source, destination)
                return f"Moved '{source}' to '{destination}'"
            except FileNotFoundError:
                return f"File not found: {source}"
            except Exception as e:
                return f"Error moving '{source}' to '{destination}': {str(e)}"
        else:
            return "Usage: mv [source] [destination]"
    else:
        return "Usage: mv [source] [destination]"
