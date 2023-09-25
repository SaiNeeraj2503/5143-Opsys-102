#!/usr/bin/env python
import subprocess
import platform
import os

def pwd(**kwargs):
    """This is my manpage entry for the pwd command
    """
    current_directory = os.getcwd()
    return current_directory
    


# if __name__=='__main__':
#     print(pwd())