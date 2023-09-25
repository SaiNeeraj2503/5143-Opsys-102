

def sort(**kwargs):
    if "params" in kwargs:
        params = kwargs["params"]
        if len(params) != 1:
            return "Usage: sort <filename>"
        else:
            filename = params[0]
            try:
                output =""
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    lines.sort()
                    sorted_content = ''.join(lines)
                    output +=sorted_content
                return output
            except FileNotFoundError:
                print(f"File not found: {filename}")
