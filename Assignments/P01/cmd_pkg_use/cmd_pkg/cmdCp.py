import shutil

def cp(**kwargs):
    if "params" in kwargs:
        params = kwargs["params"]
        if len(params) == 2:
            source = params[0]
            destination = params[1]
            try:
                shutil.copy(source, destination)
                return f"Copied '{source}' to '{destination}'"
            except FileNotFoundError:
                return f"File not found: {source}"
            except Exception as e:
                return f"Error copying '{source}' to '{destination}': {str(e)}"
        else:
            return "Usage: cp [source] [destination]"
    else:
        return "Usage: cp [source] [destination]"
