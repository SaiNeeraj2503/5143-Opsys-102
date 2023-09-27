# Define the "head" command function
def head(**kwargs):
    if "params" in kwargs:
        params = kwargs["params"]
        
        flags = kwargs["flags"]
        if "-n" in flags:
            try:
                if ".txt" in params[0]:
                    length =len(params)
                    n = int(params[length-1])
                    file_names = params[:length-1]
                else:
                    n = int(params[0])
                    file_names = params[1:]
                
                output =""
                for file_name in file_names:
                    try:
                        with open(file_name, 'r') as file:
                            lines = file.readlines()
                            
                            for line in lines[:n]:
                                output += line
                    except FileNotFoundError:
                        return f"File not found: {file_name}"
                    except Exception as e:
                        return f"Error reading {file_name}: {str(e)}"
                    return output
            except Exception as e :
                return "Usage: head -n [number] [file1] [file2] ..."
        else:
            return "Usage: head -n [number] [file1] [file2] ..."
    else:
        return "Usage: head -n [number] [file1] [file2] ..."
