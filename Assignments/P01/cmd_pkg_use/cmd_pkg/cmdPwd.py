#!/usr/bin/env python
import subprocess
import platform
import os

def pwd(**kwargs):
    """This is my manpage entry for the pwd command
    """
    if platform.system() == "Windows":
        # this runs if the os is windows
        result = subprocess.run(["cd"], stdout=subprocess.PIPE, shell=True)
        output = result.stdout.decode('utf-8')
        print(output.strip())
    else:
        # if the os is unix based, the code goes in this condition
        current_directory = os.getcwd()
        print(current_directory)
    


# if __name__=='__main__':
#     print(pwd())