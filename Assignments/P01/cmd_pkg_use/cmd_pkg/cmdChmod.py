import os
def chmod(**kwargs):
    if "params" in kwargs:
        params = kwargs["params"]
        if len(params) != 2:
            return "Usage: chmod <permissions> <filename>"
        else:
            permissions, filename = params
            try:
                # Convert the octal permissions to an integer
                permissions = int(permissions, 8)
                os.chmod(filename, permissions)
                return f"Changed permissions of '{filename}' to {oct(permissions)}"
            except ValueError:
                return "Error: Invalid permissions format (use octal, e.g., 777)"
            except FileNotFoundError:
                return f"Error: File not found: {filename}"
    else:
        return "Usage: chmod [permission] [directory_path]"
