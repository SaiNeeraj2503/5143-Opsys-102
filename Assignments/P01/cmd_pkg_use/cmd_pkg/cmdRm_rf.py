import os
import shutil

def rm(**kwargs):
    if "params" in kwargs:
        params = kwargs["params"]
        if "rf" in  kwargs["flags"][0]:
            for item in params:
                try:
                    if os.path.isdir(item):
                        shutil.rmtree(item)
                        return f"Removed directory and its contents: {item}"
                    elif os.path.isfile(item):
                        os.remove(item)
                        return f"Removed file: {item}"
                    else:
                        return f"Not found: {item}"
                except Exception as e:
                    return f"Error removing '{item}': {str(e)}"
        else:
            return "Usage: rm -rf [file_or_directory1] [file_or_directory2] ..."
    else:
        return "Usage: rm -rf [file_or_directory1] [file_or_directory2] ..."
