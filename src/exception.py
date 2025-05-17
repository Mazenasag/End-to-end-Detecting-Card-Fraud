import sys


def error_custom_details(error, error_details: sys):
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error accuerd in python script name [{0}] in line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_custom_details(
            error_message, error_details=error_details)

    def __str__(self):
        return self.error_message


try:

    result = 10/0

except Exception as e:
    raise CustomException(e, sys)
