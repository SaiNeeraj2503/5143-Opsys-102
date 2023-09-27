def cat(**kwargs):
    if "params" in kwargs:
        params = kwargs["params"]
        output =[]
        for file_name in params:
            try:
                with open(file_name, 'r') as file:
                    content = file.read()
                    output.append(content)
            except FileNotFoundError:
                return f"File not found: {file_name}"
            except Exception as e:
                return f"Error reading {file_name}: {str(e)}"
        return output
    else:
        return "Usage: cat [file1] [file2] ..."
