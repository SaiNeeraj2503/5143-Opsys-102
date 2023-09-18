#!/usr/bin/env python
import subprocess
import platform

def ls(**kwargs):
    if platform.system() == "Windows":
        command = ["powershell", "Get-ChildItem"]
        if "params" in kwargs:
            params = kwargs["params"]
            command.extend(params)
        result = subprocess.run(command, stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        lines = output.split('\n')
        file_name=""
        for line in lines[7:]:  # as the output file had 7 empty lines used this to skip those first 7 lines
            parts = line.split() 
            if len(parts) > 1:  # Check if there are more than one part (date details stuff,name)
                file_name+=parts[-1]+ "  " # Print the last part, which is the file name
        print(file_name)
    else:
        import os
        if "params" in kwargs:
            directory = kwargs["params"][0]
        else:
            directory = "."  # List the current directory by default

        try:
            files = os.listdir(directory)
            for file in files:
                print(file)  # Print the file names
        except FileNotFoundError:
            print(f"Directory not found: {directory}")
        except PermissionError:
            print(f"Permission denied: {directory}")
