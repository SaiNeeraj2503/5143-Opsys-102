def wc_w(**kwargs):
    
    if "params" in kwargs:
        params = kwargs["params"]
        if len(params) != 1:
            return "Usage: wc -w filename"
        else:
            filename = params[0]
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                    words = content.split(' ')  # Split on spaces only
                    word_count = len(words)
                    return f"Word count: {word_count}"
            except FileNotFoundError:
                return f"File not found: {filename}"
    else:
        return "Usage: wc -w [filename]"
