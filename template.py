import os
from pathlib import Path
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')

project_name = "textsummarizer"

# Define a list of file paths that need to be created
list_of_files = [
    ".github/workflows/.gitkeep",
    f"source/{project_name}/__init__.py",
    f"source/{project_name}/components/__init__.py",
    f"source/{project_name}/utils/__init__.py",
    f"source/{project_name}/utils/common.py",
    f"source/{project_name}/logging/__init__.py",
    f"source/{project_name}/config/__init__.py",
    f"source/{project_name}/config/configuration.py",
    f"source/{project_name}/pipeline/__init__.py",
    f"source/{project_name}/entity/__init__.py",
    f"source/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/notebooks.ipynb"
]

# Create directories if needed
def create_directory(directory: Path):
    try:
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {directory}")
        else:
            logging.info(f"Directory already exists: {directory}")
    except Exception as e:
        logging.error(f"Error creating directory {directory}: {e}")

# Create empty files if they don't exist
def create_empty_file(filepath: Path):
    try:
        if not filepath.exists() or filepath.stat().st_size == 0:
            filepath.touch()  # Create an empty file if it doesn't exist or is empty
            logging.info(f"Created empty file: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}")
    except Exception as e:
        logging.error(f"Error creating file {filepath}: {e}")

# Main function to ensure all directories and files exist
def setup_project_structure(files: list):
    for filepath_str in files:
        filepath = Path(filepath_str)
        filedir = filepath.parent  # Directory of the file

        # Create directories if they don't exist
        create_directory(filedir)

        # Create the empty file if it doesn't exist or is empty
        create_empty_file(filepath)

if __name__ == "__main__":
    # Call the function to set up project structure
    setup_project_structure(list_of_files)
