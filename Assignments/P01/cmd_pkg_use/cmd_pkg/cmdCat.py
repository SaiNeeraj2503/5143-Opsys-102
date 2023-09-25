def cat(**kwargs):
    if "params" in kwargs:
        params = kwargs["params"]
        for file_name in params:
            try:
                with open(file_name, 'r') as file:
                    content = file.read()
                    return content
            except FileNotFoundError:
                return f"File not found: {file_name}"
            except Exception as e:
                return f"Error reading {file_name}: {str(e)}"
    else:
        return "Usage: cat [file1] [file2] ..."
