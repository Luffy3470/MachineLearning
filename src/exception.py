import sys
from src.logger import logging

def get_error_message(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    message = "Error occurred in Python script [{0}] at line [{1}] with message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = get_error_message(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
