import os
import pathlib
from zipfile import ZipFile

def write_output(ingredients, input_filename):
    create_zip()
    with open(f'../outputs/{input_filename[:-6]}out.txt', 'w') as f:
        f.write(str(len(ingredients))+" "+' '.join(str(x) for x in ingredients))



def create_zip():
    pathlib.Path('../outputs').mkdir(parents=True, exist_ok=True) 
    with ZipFile('../outputs/src.zip', 'w') as myzip:
        for file in os.listdir(os.curdir):
            myzip.write(file)

