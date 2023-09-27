#!/usr/bin/env python
import subprocess
import platform
import os

import time

def mode_to_string(mode):
    # Convert a file mode to an "rwx" string
    perms = ["---", "--x", "-w-", "-wx", "r--", "r-x", "rw-", "rwx"]
    #return perms[int(mode[2])] + perms[int(mode[3])] + perms[int(mode[4])]
    return perms[(mode >> 6) & 7] + perms[(mode >> 3) & 7] + perms[mode & 7]

def format_size(size):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    index = 0
    while size >= 1024 and index < len(units) - 1:
        size /= 1024.0
        index += 1
    return f"{size:.1f} {units[index]}"

def ls(**kwargs):
    
    if "params" in kwargs:
        if len(kwargs["params"]) > 0:
            directory = kwargs["params"][0]
        else:
            directory = os.getcwd()
    

    else:
        directory = "."  # List the current directory by default
    
    show_hidden = False
    human_readable = False
    long_listing = False

    if "flags" in kwargs:
        flags = kwargs["flags"]
        for flag in flags:
            if "a" in flag:
                show_hidden = True
            if "h" in flag:
                human_readable = True
            if "l" in flag:
                long_listing =True
    try:
        files = os.listdir(directory)
        output = []
      # Check for flags
        if long_listing:
            # Handle -l flag (long format)
            for file in files:
                if not show_hidden and file.startswith("."):
                    continue
                file_stat = os.stat(os.path.join(directory, file))
                mode = file_stat.st_mode
                #permissions = mode_to_string(oct(file_stat.st_mode & 0o777))  # Convert mode to "rwx" format
                permissions = mode_to_string(file_stat.st_mode)
                num_links = file_stat.st_nlink
                owner = file_stat.st_uid
                group = file_stat.st_gid
                size = file_stat.st_size
                if human_readable:
                    size= format_size(size)
                date_modified = file_stat.st_mtime
                formatted_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(date_modified))
                output.append(f"{permissions} {num_links} {owner} {group} {size} {formatted_date} {file}")
            return "\n".join(output)
            # elif "a" in kwargs:
            #     # Handle -a flag (include hidden files)
            #     for file in files:
            #         output.append(file)
            # elif "h" in kwargs:
            #     # Handle -h flag (human-readable sizes)
            #     for file in files:
            #         file_stat = os.stat(os.path.join(directory, file))
            #         size = file_stat.st_size
            #         size_str = ""
            #         for unit in ['B', 'KB', 'MB', 'GB']:
            #             if size < 1024.0:
            #                 size_str = f"{size:.1f} {unit}"
            #                 break
            #             size /= 1024.0
            #         output.append(f"{size_str} {file}")
        else:
            # Default behavior (list visible files)
            for file in files:
                if not show_hidden and file.startswith("."):
                    continue
                output.append(file)
            return "  ".join(output)

        
    except FileNotFoundError:
        return f"Directory not found: {directory}"
    except PermissionError:
        return f"Permission denied: {directory}"

