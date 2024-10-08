# config.py
# Version 1.0: Central configuration for project paths

import os

# Dynamically determine the project root based on the location of this file
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
QUOTES_DIR = os.path.join(PROJECT_ROOT, "quotes")
