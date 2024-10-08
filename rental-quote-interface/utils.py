# utils.py
# Version 1.0: Utility functions for managing paths and working directory

import os
from config import PROJECT_ROOT

def set_working_directory():
    """
    Sets the current working directory to the project root.
    """
    if os.getcwd() != PROJECT_ROOT:
        os.chdir(PROJECT_ROOT)
        print(f"Working directory set to project root: {os.getcwd()}")
    else:
        print(f"Working directory is already set to project root: {os.getcwd()}")
