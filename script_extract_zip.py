from zipfile import ZipFile
import os


def extract_data_from_zip(zip_patch):
    with ZipFile(zip_patch, 'r') as reader:
        reader.extractall(os.path.join(os.path.dirname(os.getcwd()), 'resources'))

