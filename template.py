import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

#logging.info("Hello every one this is logging framework")

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "app.py",
   
]

for filepath in list_of_files:
    # Below line is used based on operating system taking the format
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    #print(filename)

# creating the directorys
    if filedir!="":
         os.makedirs(filedir,exist_ok=True)
         logging.info(f"creating directory {filedir} for this files {filename}")

    # creating the files
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
            with open(filepath,"w") as f:
                logging.info(f"creating empty files: {filepath}")

    else:
            logging.info(f"{filename} already exist")


    
