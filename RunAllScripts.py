#The purpose of this file is to convert multiple files stored as Python notebook code to new files in PY format. Then, run all of the scripts.

import subprocess

#List the names of the Jupyter Notebook files you want to run
files_to_run = ["File1.ipynb", "File2.ipynb", "File3.ipynb", "File4.ipynb", "File5.ipynb"]

#Loop through the list of files and convert each notebook to a Python script
for file in files_to_run:
    subprocess.run(["jupyter", "nbconvert", "--to", "python", file])

#List the names of the Python script files that were generated
python_scripts = ["File1.py", "File2.py", "File3.py", "File4.py", "File5.py"]

#Loop through the list of Python scripts and run each one
for script in python_scripts:
    subprocess.run(["python", script])


