def wc(**kwargs):
    
    if "params" in kwargs:
        params = kwargs["params"]
        flags = kwargs["flags"]
        if len(params) < 1:
            return "Usage: wc -w filename or wc -l filename"
        if flags[0] not in ['-w','-l']:
            return "Usage: wc -w filename or wc -l filename"
        else:
            filename = params[0]
            try:
                with open(filename, 'r') as file:
                      # Split on spaces only
                    word_count=0
                    lines = file.readlines()
                    for line in lines:
                        
                        words = line.split(' ')
                        
                        word_count+=len(words)
                    if "l" in flags[0]:
                        return f"Lines count: {len(lines)}"
                    else:
                        return f"words count: {word_count}"
            except FileNotFoundError:
                return f"File not found: {filename}"
    else:
        return "Usage: wc -w [filename]"
