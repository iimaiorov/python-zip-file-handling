import os
import pytest
import shutil


from script_archive_zip import archive_data_to_zip
from script_extract_zip import extract_data_from_zip

PROJECT_RESOURCES_PATH = os.path.join(os.path.dirname(os.getcwd()), 'resources')
PROJECT_DATA_PATH = os.path.join(os.path.dirname(os.getcwd()), 'data')
ZIP_FILE_NAME = 'data.zip'


@pytest.fixture(autouse=True)
def data_manager():
    archive_data_to_zip(PROJECT_DATA_PATH, PROJECT_RESOURCES_PATH, ZIP_FILE_NAME)
    extract_data_from_zip(PROJECT_RESOURCES_PATH+'\\'+ZIP_FILE_NAME)
    yield
    shutil.rmtree(PROJECT_RESOURCES_PATH)
    os.mkdir(PROJECT_RESOURCES_PATH)
