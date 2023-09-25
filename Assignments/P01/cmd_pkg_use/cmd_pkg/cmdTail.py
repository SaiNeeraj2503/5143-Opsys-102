# Define the "head" command function
def tail(**kwargs):
    if "params" in kwargs:
        params = kwargs["params"]
        flags = kwargs["flags"]
        if "-n" in flags:
            try:
                #n_index = params.index("-n")
                n = int(params[0])
                file_names = params[1:]

                for file_name in file_names:
                    lis =[]
                    try:
                        with open(file_name, 'r') as file:
                            lines = file.readlines()
                            for line in lines[-n:]:
                                lis.append(line.rstrip('\n'))
                    except FileNotFoundError:
                        lis.append(f"File not found: {file_name}")
                    except Exception as e:
                        lis.append(f"Error reading {file_name}: {str(e)}")
                    return '\n'.join(lis)
            except (ValueError, IndexError):
                return "Usage: tail -n [number] [file1] [file2] ..."
        else:
            return "Usage: tail -n [number] [file1] [file2] ..."
    else:
        return "Usage: tail -n [number] [file1] [file2] ..."
