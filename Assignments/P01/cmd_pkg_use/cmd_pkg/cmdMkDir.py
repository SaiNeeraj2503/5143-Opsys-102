import os

def mkdir(**kwargs):
    if "params" in kwargs:
        params = kwargs["params"]
        for directory_name in params:
            try:
                os.mkdir(directory_name)
                return f"Directory '{directory_name}' created successfully."
            except FileExistsError:
                return f"Directory '{directory_name}' already exists."
            except Exception as e:
                return f"Error creating directory '{directory_name}': {str(e)}"
    else:
        return "Usage: mkdir [directory_name1] [directory_name2] ..."
