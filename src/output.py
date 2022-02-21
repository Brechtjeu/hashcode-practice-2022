import os
from zipfile import ZipFile


def create_zip():
    with ZipFile('../outputs/src.zip', 'w') as myzip:
        for file in os.listdir(os.curdir):
            myzip.write(file)