import os

def cd(**kwargs):
    if "params" in kwargs:
        params = kwargs["params"]
        if len(params) > 0:
            try:
                if params[0] == "~":
                    os.chdir(os.path.expanduser("~"))  # Change to the user's home directory
                else:
                    os.chdir(params[0])
                return f"Current directory changed to: {os.getcwd()}"
            except FileNotFoundError:
                return f"Directory not found: {params[0]}"
            except Exception as e:
                return f"Error changing directory: {str(e)}"
        else:
            return "Usage: cd [directory_path]"
    else:
        return "Usage: cd [directory_path]"
