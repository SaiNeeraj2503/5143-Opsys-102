# Define the "head" command function
def head(**kwargs):
    if "params" in kwargs:
        params = kwargs["params"]
        if "-n" in params:
            try:
                n_index = params.index("-n")
                n = int(params[n_index + 1])
                file_names = params[:n_index] + params[n_index + 2:]

                for file_name in file_names:
                    try:
                        with open(file_name, 'r') as file:
                            lines = file.readlines()
                            output =""
                            for line in lines[:n]:
                                output += line
                    except FileNotFoundError:
                        return f"File not found: {file_name}"
                    except Exception as e:
                        return f"Error reading {file_name}: {str(e)}"
            except (ValueError, IndexError):
                return "Usage: head -n [number] [file1] [file2] ..."
        else:
            return "Usage: head -n [number] [file1] [file2] ..."
    else:
        return "Usage: head -n [number] [file1] [file2] ..."
