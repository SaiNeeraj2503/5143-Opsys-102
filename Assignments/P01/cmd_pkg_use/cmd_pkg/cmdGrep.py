# cmd_pkg/cmdGrepL.py

def grep(**kwargs):
    if "params" in kwargs:
        params = kwargs["params"]
        flags = kwargs["flags"]
        if len(params) != 2 or flags[0] != '-l':
            return "Usage: grep -l pattern filename"
        else:
            pattern= params[0].strip('\'"')
            filename=params[1]
            
            try:
                matching_files = []
                with open(filename, 'r') as file:
                    for line in file:
                        if pattern in line:
                            matching_files.append(filename)
                            
                            break  # Break after the first match is found

                if matching_files:
                    return f"Files containing '{pattern}': {', '.join(matching_files)}"
            except FileNotFoundError:
                return f"File not found: {filename}"
