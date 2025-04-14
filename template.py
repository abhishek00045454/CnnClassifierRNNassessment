import os
from pathlib import Path
import logging
import subprocess
import sys

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:', force=True)

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

def create_project_structure():
    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir} for file: {filename}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, 'w') as f:
                pass  # create an empty file
            logging.info(f"Creating empty file: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}")

def create_virtual_env():
    venv_dir = "venv"
    if not os.path.exists(venv_dir):
        logging.info("Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
        logging.info("Virtual environment created at ./venv")
    else:
        logging.info("Virtual environment already exists")

# 👇 This ensures the code runs only when you execute the script directly
if __name__ == "__main__":
    print("Starting project setup...")
    create_project_structure()
    create_virtual_env()
    print("✅ Project structure and virtual environment setup complete.")
