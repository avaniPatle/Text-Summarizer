import os
from pathlib import Path
import logging #logs during runtime

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github.com/workflows/.gitkeep", #used for CICD deployment / yaml files
    f"src/{project_name}/__init__.py", #constructor file is __init__|| like if u want to create own library and import it like from textSummarizer import myOwnLibrary 
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py", 
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py", #local package setup
    "research/trials.ipynb"
]

# windows uses backward slash not /, so we use Path from pathlib

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) # will return folder and file
    #make sure filedir is not empty
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: '{filedir}' for file '{filename}'.")    
  
    # make file - check if there or not 0 bytes
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Created empty file: '{filepath}'.")
    else:
        logging.info(f"File '{filepath}' already exists.")