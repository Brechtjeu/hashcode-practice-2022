import os
import pathlib
from zipfile import ZipFile

def create_zip():
    pathlib.Path('../outputs').mkdir(parents=True, exist_ok=True) 
    with ZipFile('../outputs/src.zip', 'w') as myzip:
        for file in os.listdir(os.curdir):
            myzip.write(file)

