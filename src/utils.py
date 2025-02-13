#A utils file in a Python project serves as a central location for storing utility functions and
# code that can be reused across different parts of the project. The purpose of a utils file is to promote code reusability, maintainability, and organization within a Python project.


import os,sys

import numpy as np
import pandas as pd
import dill

from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj, file_obj)

    except:
        raise CustomException(e,sys)

