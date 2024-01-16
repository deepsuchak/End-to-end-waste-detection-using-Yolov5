import os
from pathlib import Path
import logging

## which time we executed and what message
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")


project_name = "wastedetection"

list_of_files = [
    '.github/workflows/.gitkeep', ## for github action, gitkeep is a temp file
    'data/.gitkeep', ## user will upload as input that image will be saved here
    f'{project_name}/__init__.py', ## constructor file as a local package
    f'{project_name}/components/__init__.py',
    f'{project_name}/components/data_ingestion.py', ## Yolov5 automatically does data_transformation
    f'{project_name}/components/data_validation.py', 
    f'{project_name}/components/model_trainer.py',
    f'{project_name}/constant/__init__.py',
    f'{project_name}/constant/training_pipeline/__init__.py',
    f'{project_name}/constant/applcation.py',
    f'{project_name}/entity/config_entity.py',
    f'{project_name}/entity/artifacts_entity.py',
    f'{project_name}/exception/__init__.py',
    f'{project_name}/logger/__init__.py',
    f'{project_name}/pipeline/__init__.py',
    f'{project_name}/pipeline/training_pipeline.py',
    f'{project_name}/utils/__init__.py',
    f'{project_name}/utils/main_utils.py',
    'templates/index.html',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
]

for filepath in list_of_files:
    ## we have used forward slash above, so the Path class will automatically detect the OS and convert it to that path
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")


    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} already exists!")
# ## Iterates through each file path in the list of files.
# Converts the file path to a Path object, ensuring compatibility with the operating system's path format.
# Uses os.path.split() to separate the file path into the directory (filedir) and the filename (filename).
# Checks if the directory (filedir) is not empty. If it's not empty, it creates the directory using os.makedirs if it doesn't already exist and logs the creation.
# Checks if the file (filename) does not exist or if its size is 0 bytes. If either condition is true, it creates an empty file using open() with mode "w" and logs the creation.
# If the file already exists and is not empty, it logs that the file already exists.

    