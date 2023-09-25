#!/usr/bin/env python
import subprocess
import platform
import os

def ls(**kwargs):
    if "params" in kwargs:
        if len(kwargs["params"]) > 1:
            directory = kwargs["params"][0]
        else:
            dir = kwargs["params"] 
            directory= os.getcwd()
    else:
        directory = "."  # List the current directory by default

    try:
        files = os.listdir(directory)
        output = []
        for file in files:
            output.append(file)   # Print the file names
        return output
    except FileNotFoundError:
        return f"Directory not found: {directory}"
    except PermissionError:
        return f"Permission denied: {directory}"

# Example usage:
ls(params=["/path/to/directory"])
