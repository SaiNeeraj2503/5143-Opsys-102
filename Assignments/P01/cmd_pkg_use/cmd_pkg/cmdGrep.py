# cmd_pkg/cmdGrepL.py

def grep(**kwargs):
    if "params" in kwargs:
        params = kwargs["params"]
        flags = kwargs["flags"]
        if len(flags) != 0:
            for f in flags:
                if f not in ["-l"]:
                    return "Usage: grep  pattern filename or grep -l pattern filename"
        if len(params) < 2:
            return "Usage: grep -l pattern filename"
        else:
            pattern= params[0].strip('\'"')
            files=params[1:]
            try:
                matching_files = []
                for filename in files:
                    with open(filename, 'r') as file:
                        for line in file:
                            if pattern in line:
                                matching_files.append(filename)
                                
                                break  # Break after the first match is found

                if matching_files:
                    if len(flags) != 0:
                        if flags[0] == "-l":
                          return matching_files
                    return f"Files containing '{pattern}': {', '.join(matching_files)}"
            except FileNotFoundError:
                return f"File not found: {filename}"
